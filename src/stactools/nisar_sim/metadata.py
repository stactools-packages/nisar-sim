import os
import re
from datetime import datetime
from typing import Any, Dict, List, Tuple, TypeVar

import fsspec
import h5py
import pystac
from pystac.extensions.sat import SatExtension
from pystac.utils import str_to_datetime
from shapely.geometry import mapping
from shapely.wkt import loads

T = TypeVar("T", pystac.Item, pystac.Asset)


class H5MetadataException(Exception):
    pass


class AnnotatedMetadataException(Exception):
    pass


class MetadataLinks:
    """Generates the correct paths to metadata files"""

    def __init__(self, href: str, dither: str, nmode: str) -> None:
        self.asset_href = href
        self.dither = dither
        self.nmode = nmode
        self.id = os.path.basename(os.path.normpath(href))

        self.h5_href = self._href_modifier(href, extension=".h5", nmode=nmode)
        self.ann_a_href = self._href_modifier(href, extension=".ann", nmode=f"{nmode}A")
        self.ann_b_href = self._href_modifier(href, extension=".ann", nmode=f"{nmode}B")

    def _replace_dither(self, id: str, dither: str) -> str:
        id_pattern = r"_([CX])([DGX])_"
        return re.sub(id_pattern, f"_\\1{dither}_", id)

    def _href_modifier(
        self,
        href: str,
        extension: str,
        nmode: str,
    ) -> str:
        _id = self._replace_dither(self.id, self.dither)
        path = href.strip("/") + "/" + _id + "." + extension.lstrip(".")
        path_parts = str(path).split("_")
        path_parts.insert(-1, nmode)
        path = "_".join(path_parts)
        return str(path)


class HDF5Metadata:
    """Reads HDF5 file into a usable h5py object"""

    def __init__(self, h5_href: str) -> None:
        self.href = h5_href
        self.metadata = self.from_file(self.href)

    def from_file(self, href: str) -> Any:
        fs = fsspec.open(href)
        return h5py.File(fs.open(), "r")


class AnnotatedMetadata:
    """Reads annotation file into a usable dict"""

    def __init__(self, ann_a_href: str, ann_b_href: str) -> None:
        self.ann_a_href = ann_a_href
        self.ann_b_href = ann_b_href
        self.metadata_a = self.parse_ann(self.ann_a_href)
        self.metadata_b = self.parse_ann(self.ann_b_href)

    def parse_ann(self, ann_href: str) -> Dict[str, Any]:
        """Reads in annotated file location and returns dict of key-value pairs
        Strips out comments, spacing, and units
        Args:
            ann_href (str):

        Example:
            DEM Datum                                         (&)         = WGS-84
            becomes {"DEM_Datum": "WGS-84"}
        """
        with fsspec.open(ann_href, "r") as f:
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
    def __init__(self, href: str, id: str, h5_metadata: Any, ann_metadata: Any) -> None:
        self.href = href
        self.base_id = "_".join(id.split("_")[:-2])
        self.h5_metadata = h5_metadata
        self.ann_metadata = ann_metadata

        def _get_geometries() -> Tuple[List[float], Dict[str, Any]]:
            h5_polygon = self.h5_metadata.metadata["science"]["LSAR"][
                "identification"
            ].get("boundingPolygon")
            if not h5_polygon:
                raise H5MetadataException(
                    f"Unable to locate boundingPolygon for {self.h5_metadata.href}"
                )
            polygon = loads(h5_polygon[()])
            geometry = mapping(polygon)
            bbox = list(polygon.bounds)

            return (bbox, geometry)

        self.bbox, self.geometry = _get_geometries()

    @property
    def start_datetime(self) -> datetime:
        if start_time := self.h5_metadata.metadata["science"]["LSAR"][
            "identification"
        ].get("zeroDopplerStartTime"):
            return str_to_datetime(start_time[()])
        else:
            raise ValueError(
                "Cannot determine product start time using H5 metadata "
                f" at {self.h5_metadata.href}"
            )

    @property
    def end_datetime(self) -> datetime:
        if end_time := self.h5_metadata.metadata["science"]["LSAR"][
            "identification"
        ].get("zeroDopplerEndTime"):
            return str_to_datetime(end_time[()])
        else:
            raise ValueError(
                "Cannot determine product end time using H5 metadata "
                f" at {self.h5_metadata.href}"
            )

    @property
    def get_datetime(self) -> datetime:
        start_time = self.start_datetime
        end_time = self.end_datetime

        if all([start_time, end_time]):
            set_time = start_time + (end_time - start_time) / 2

        if not set_time:
            raise ValueError(
                "Cannot determine product datetime using H5 metadata "
                f" at {self.h5_metadata.href}"
            )
        else:
            return str_to_datetime(str(set_time))

    @property
    def inventory(self) -> List[str]:
        files: List[str] = []
        for metadata in [self.ann_metadata.metadata_a, self.ann_metadata.metadata_b]:
            files.extend(v for k, v in metadata.items() if self.base_id in v)
        if not files:
            raise AnnotatedMetadataException(
                "Cannot determine product files using annotated metadata at "
                f"{self.ann_metadata.ann_a_href} or {self.ann_metadata.ann_b_href}"
            )
        files.extend(
            [
                os.path.basename(self.ann_metadata.ann_a_href),
                os.path.basename(self.ann_metadata.ann_b_href),
            ]
        )
        return files


def fill_sat_properties(sat_ext: SatExtension[T], h5_data: Any) -> None:
    """Fills the properties for SAT
    Based on the sat Extension.py
    Args:
        sat_ext (SarExtension): The extension to be populated
        h5_data (Any): h5 file object
    """

    if absolute_orbit := h5_data["science"]["LSAR"]["identification"].get(
        "absoluteOrbitNumber"
    ):
        sat_ext.absolute_orbit = int(absolute_orbit[()])  # stored as numpy.uint32
