import logging
import re

from pystac import Collection, Item, Summaries
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.sar import SarExtension
from pystac.extensions.sat import SatExtension

from stactools.nisar_sim import constants as c
from stactools.nisar_sim.metadata import (
    AnnotatedMetadata,
    HDF5Metadata,
    Metadata,
    MetadataLinks,
    fill_sar_properties,
    fill_sat_properties,
)
from stactools.nisar_sim.nisar_assets import get_assets

# import rasterio


logger = logging.getLogger(__name__)


def create_collection() -> Collection:
    """Create a STAC Collection

    This function includes logic to extract all relevant metadata from
    an asset describing the STAC collection and/or metadata coded into an
    accompanying constants.py file.

    See `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_.

    Returns:
        Collection: STAC Collection object
    """
    summary_dict = {
        "platform": c.NISAR_SIM_PLATFORMS,
    }

    collection = Collection(
        id="nisar-sim",
        title="Simulated NISAR",
        description=c.NISAR_SIM_DESCRIPTION,
        providers=c.NISAR_SIM_PROVIDERS,
        extent=c.NISAR_SIM_EXTENT,
        summaries=Summaries(summary_dict),
        stac_extensions=[
            ItemAssetsExtension.get_schema_uri(),
            ProjectionExtension.get_schema_uri(),
            SarExtension.get_schema_uri(),
            # SatExtension.get_schema_uri(),
        ],
        keywords=c.NISAR_SIM_KEYWORDS,
    )

    # Links
    collection.add_links(c.NISAR_SIM_LINKS)

    # SAR Extension
    sar = SarExtension.summaries(collection, add_if_missing=True)
    sar.looks_range = c.NISAR_SIM_SAR["looks_range"]
    sar.product_type = c.NISAR_SIM_SAR["product_type"]
    sar.looks_azimuth = c.NISAR_SIM_SAR["looks_azimuth"]
    sar.polarizations = c.NISAR_SIM_SAR["polarizations"]
    sar.frequency_band = c.NISAR_SIM_SAR["frequency_band"]
    sar.instrument_mode = c.NISAR_SIM_SAR["instrument_mode"]
    sar.center_frequency = c.NISAR_SIM_SAR["center_frequency"]
    # sar.resolution_range = c.NISAR_SIM_SAR["resolution_range"]
    # sar.resolution_azimuth = c.NISAR_SIM_SAR["resolution_azimuth"]
    # sar.pixel_spacing_range = c.NISAR_SIM_SAR["pixel_spacing_range"]
    # sar.pixel_spacing_azimuth = c.NISAR_SIM_SAR["pixel_spacing_azimuth"]
    # sar.looks_equivalent_number = c.NISAR_SIM_SAR["looks_equivalent_number"]

    # sat = SatExtension.summaries(collection, add_if_missing=True)
    # sat.absolute_orbit = c.NISAR_SIM_SAT["absolute_orbit"]

    assets = ItemAssetsExtension.ext(collection, add_if_missing=True)
    assets.item_assets = get_assets(collection=True)

    return collection


def create_item(product_path: str, dither: str) -> Item:
    """Create a STAC Item

    Args:
        product_href (str): An HREF data directory pointing to a flight
        dither (str): Type of dither ("X","G","D")
            X: No Dither
            G: Dither with gaps
            D: Dithered without gaps

    Returns:
        Item: STAC Item object
    """
    dither = dither.upper()
    if dither not in ["X", "G", "D"]:
        raise ValueError("Dither value not valid")

    metalinks = MetadataLinks(product_path, dither)
    h5_data = HDF5Metadata(metalinks.h5_href)
    ann_data = AnnotatedMetadata(metalinks.ann_href)
    metadata = Metadata(product_path, metalinks.id, h5_data, ann_data)

    item = Item(
        id=metalinks.id,
        properties={},
        geometry=metadata.geometry,
        bbox=metadata.bbox,
        datetime=metadata.get_datetime,
        stac_extensions=[],
    )

    proj_attrs = ProjectionExtension.ext(item, add_if_missing=True)
    proj_attrs.epsg = 4326

    # proj_attrs.shape = [1, 1]  # TODO: KMZ?
    # proj_attrs.transform = [-180, 360, 0, 90, 0, 180]  # TODO: KMZ?

    get_xtalk = re.search(r"_(\w)\w_", metalinks.id)
    xtalk = get_xtalk.group(1) if get_xtalk else "C"
    version = metalinks.id.rsplit("_", 1)[1]

    expected_assets = get_assets(dither=dither, xtalk=xtalk)
    expected_assets_with_versions = {
        f"{k.split('.')[0]}_{version}.{k.split('.')[1]}": v
        for k, v in expected_assets.items()
    }

    for key, value in metadata.inventory.items():
        base_id = len(metadata.base_id)  # lint work around
        if (
            asset_def := expected_assets_with_versions.get(value[base_id:].lstrip("_"))
        ) is not None:
            asset = asset_def.create_asset((value))
            item.add_asset(key, asset)

    # SAR extension
    sar = SarExtension.ext(item, add_if_missing=True)
    fill_sar_properties(sar, h5_data.metadata)

    # SAT extension
    sat = SatExtension.ext(item, add_if_missing=True)
    fill_sat_properties(sat, h5_data.metadata)

    return item
