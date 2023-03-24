import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import h5py
from pystac.utils import str_to_datetime
from shapely.geometry import mapping
from shapely.wkt import loads

# from stactools.nisar_sim import constants as c


class MetadataLinks:
    """Generates the correct paths to metadata files"""

    def __init__(self, href: str, dither: str) -> None:
        self.asset_href = href
        self.dither = dither
        self.id = os.path.basename(os.path.normpath(href))
        self.h5_href = self._href_modifier(href, extension=".h5")
        self.ann_href = self._href_modifier(href, extension=".ann", frequency="129A")

    def _replace_dither(self, id: str, dither: str) -> str:
        id_pattern = r"_([CX])([DGX])_"
        result = re.sub(
            id_pattern, f"_\\1{dither}_", id
        )  # lambda match: f"_{match.group(1)}{dither}_"
        return result

    def _href_modifier(
        self,
        href: str,
        extension: Optional[str] = None,
        frequency: Optional[str] = None,
    ) -> str:
        id = self._replace_dither(self.id, self.dither)
        path = Path(href) / id

        if extension:
            path = path.with_suffix(extension)
        if frequency is not None:
            path_parts = str(path).split("_")
            path_parts.insert(-1, frequency)
            path = Path("_".join(path_parts))
        return str(path)


class HDF5Metadata:
    """Reads HDF5 file into a usable h5py object"""

    def __init__(self, h5_href: str) -> None:
        self.href = h5_href
        self.metadata = self.from_file(self.href)

    def from_file(self, href: str) -> Any:
        return h5py.File(href, "r")


class AnnotatedMetadata:
    """Reads annotation file into a usable dict"""

    def __init__(self, ann_href: str) -> None:
        self.href = ann_href
        self.metadata = self.parse_ann(self.href)

    def parse_ann(self, ann_href: str) -> Dict[str, Any]:
        """Reads in annotated file location and returns dict of key-value pairs
        Strips out comments, spacing, and units
        Args:
            ann_href (str):

        Example:
            DEM Datum                                         (&)         = WGS-84
            becomes {"DEM_Datum": "WGS-84"}
        """
        with open(ann_href, "r") as f:
            lines = f.readlines()
            data = {}
            for line in lines:
                if "=" in line:
                    key_value = line.split("=", 1)
                    key = (
                        re.sub(r"^[^a-zA-Z]*", "", key_value[0])
                        .split("(")[0]
                        .strip()
                        .replace(" ", "_")
                    )
                    value = key_value[1].split(";")[0].strip()
                    data[key] = value
        return data


class Metadata:
    def __init__(
        self, href: str, id: str, h5_metadata: Any, ann_metadata: Dict[str, Any]
    ) -> None:
        self.href = href
        self.versionless_id = id[: id.rfind("_")]
        self.h5_metadata = h5_metadata
        self.ann_metadata = ann_metadata

        def _get_geometries() -> Tuple[List[float], Dict[str, Any]]:
            h5_polygon = self.h5_metadata["science"]["LSAR"]["identification"][
                "boundingPolygon"
            ]
            polygon = loads(h5_polygon[()])
            geometry = mapping(polygon)
            bbox = list(polygon.bounds)

            return (bbox, geometry)

        self.bbox, self.geometry = _get_geometries()

    @property
    def start_datetime(self) -> datetime:
        start_time = self.h5_metadata["science"]["LSAR"]["identification"][
            "zeroDopplerStartTime"
        ]
        if start_time is None:
            raise ValueError(
                "Cannot determine product start time using H5 metadata "
                f" at {self.href}"
            )
        else:
            return str_to_datetime(start_time[()])

    @property
    def end_datetime(self) -> datetime:
        end_time = self.h5_metadata["science"]["LSAR"]["identification"][
            "zeroDopplerEndTime"
        ]
        if end_time is None:
            raise ValueError(
                "Cannot determine product end time using H5 metadata "
                f" at {self.href}"
            )
        else:
            return str_to_datetime(end_time[()])

    @property
    def get_datetime(self) -> datetime:
        start_time = self.start_datetime
        end_time = self.end_datetime

        if all([start_time, end_time]):
            set_time = start_time + (end_time - start_time) / 2

        if set_time is None:
            raise ValueError(
                "Cannot determine product datetime using H5 metadata "
                f" at {self.href}"
            )
        else:
            return str_to_datetime(str(set_time))

    @property
    def inventory(self) -> Dict[str, str]:
        files = {k: v for k, v in self.ann_metadata.items() if self.versionless_id in v}

        if files is None:
            raise ValueError(
                "Cannot determine product files using annotated metadata "
                f" at {self.href}"
            )
        else:
            return files
