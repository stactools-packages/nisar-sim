import logging
import re

from pystac import Collection, Item, Summaries
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.sat import SatExtension

from stactools.nisar_sim import constants as c
from stactools.nisar_sim.metadata import (
    AnnotatedMetadata,
    HDF5Metadata,
    Metadata,
    MetadataLinks,
    fill_sat_properties,
)
from stactools.nisar_sim.nisar_assets import get_assets

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
            SatExtension.get_schema_uri(),
        ],
        keywords=c.NISAR_SIM_KEYWORDS,
    )

    # Links
    collection.add_links(c.NISAR_SIM_LINKS)

    assets = ItemAssetsExtension.ext(collection, add_if_missing=True)
    assets.item_assets = get_assets(collection=True)

    return collection


def create_item(product_href: str, dither: str, nmode: str) -> Item:
    """Create a STAC Item

    Args:
        product_href (str): An HREF data directory pointing to a flight
        dither (str): Type of dither ("X","G","D")
            X: No Dither
            G: Dither with gaps
            D: Dithered without gaps
        nmode (str): set of numbers associated with a specific center frequency,
            bandwidth, and polarization ("129","138","143")

    Returns:
        Item: STAC Item object
    """
    metalinks = MetadataLinks(product_href, dither, nmode)
    h5_data = HDF5Metadata(metalinks.h5_href)
    ann_data = AnnotatedMetadata(metalinks.ann_a_href, metalinks.ann_b_href)
    metadata = Metadata(product_href, metalinks.id, h5_data, ann_data)

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

    get_xtalk = re.search(r"_(\w)\w_", metalinks.id)
    xtalk = get_xtalk[1] if get_xtalk else "C"

    expected_assets = get_assets(dither=dither, xtalk=xtalk)

    # fmt: off
    def asset_name(name: str) -> str:
        versionless = name[:name.rfind("_")] + name[name.find("."):]
        return versionless[len(metadata.base_id):].lstrip("_")
    # fmt: on

    for _file in metadata.inventory:
        if asset_def := expected_assets.get(asset_name(_file)):
            asset = asset_def.create_asset(_file)
            item.add_asset(asset_name(_file), asset)

    # SAT extension
    sat = SatExtension.ext(item, add_if_missing=True)
    fill_sat_properties(sat, h5_data.metadata)

    return item
