from os import path
from typing import Any, Dict, List, Tuple, TypeVar

import fsspec
import h5py
from pystac import Asset, Item, MediaType
from pystac.extensions.item_assets import AssetDefinition
from shapely.geometry import mapping
from shapely.wkt import loads
from stactools.nisar_sim import constants as c

T = TypeVar("T", Item, Asset)


class MetadataException(Exception):
    pass


class Metadata:
    def __init__(self, href: str) -> None:
        self.href = href
        self.id = path.splitext(path.basename(href))[0]
        self.get_metadata(href)

    def get_metadata(self, href: str) -> None:
        with fsspec.open(href, "rb") as f:
            with h5py.File(f, "r") as h5_data:

                def get_geometry(
                    h5_data: h5py.File,
                ) -> Tuple[Dict[str, Any], List[float]]:
                    h5_polygon = h5_data["science"]["LSAR"]["identification"].get(
                        "boundingPolygon"
                    )
                    if not h5_polygon:
                        raise MetadataException("Unable to locate boundingPolygon")
                    polygon = loads(h5_polygon[()])
                    geometry = mapping(polygon)
                    bbox = list(polygon.bounds)

                    return geometry, bbox

                self.geometry, self.bbox = get_geometry(h5_data)

                # Satellite Extension (Sat)
                if absolute_orbit := h5_data["science"]["LSAR"]["identification"].get(
                    "absoluteOrbitNumber"
                ):
                    self.absolute_orbit = int(absolute_orbit[()])


def filename_convention(source: str) -> Dict[str, Any]:
    """
    Parse the filename to extract metadata
    """

    import re
    from datetime import datetime

    from pystac.extensions.sat import OrbitState

    filename = path.basename(source)

    filename_convention = (
        r"NISAR_(?P<instrument>[L|S])(?P<level>[0-3])_(?P<processing_type>(PR|UR))_"
        r"(?P<product_identifier>(RRSD|RIFG|ROFF|RSLC|RUNW|GCOV|COFF|GSLC|GUNW|SME2))_"
        r"\d{3}_\d{3}_(?P<orbit_state>[A|D])_\d{3}\w?_.*"
        r"(?P<start_datetime>\d{8}T\d{6})_(?P<end_datetime>\d{8}T\d{6}).*"
    )
    matches = re.match(filename_convention, filename)
    if not matches:
        raise MetadataException(f"Unable to parse filename {filename}")

    date_format = "%Y%m%dT%H%M%S"
    product_type = matches.group("product_identifier")

    additional_info = {
        "type": product_type,
        "title": c.NISAR_PRODUCTS.get(product_type, {}).get("title"),
        "description": c.NISAR_PRODUCTS.get(product_type, {}).get("description"),
        "start_datetime": datetime.strptime(matches["start_datetime"], date_format),
        "end_datetime": datetime.strptime(matches["end_datetime"], date_format),
        "orbit_state": OrbitState.ASCENDING
        if matches["orbit_state"] == "A"
        else OrbitState.DESCENDING,
    }

    return {**matches.groupdict(), **additional_info}


def fill_item_assets() -> Dict[str, AssetDefinition]:
    assets = {}
    for product in c.NISAR_PRODUCTS:
        assets[product] = AssetDefinition(
            {
                "title": c.NISAR_PRODUCTS[product]["title"],
                "description": c.NISAR_PRODUCTS[product]["description"],
                "type": MediaType.HDF5,
                "role": ["data"],
            }
        )

    return assets
