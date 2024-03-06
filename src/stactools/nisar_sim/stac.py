import logging

from pystac import Asset, Collection, Item, MediaType, Summaries
from pystac.extensions.item_assets import ItemAssetsExtension
from pystac.extensions.projection import ProjectionExtension
from pystac.extensions.sat import SatExtension
from stactools.nisar_sim import constants as c
from stactools.nisar_sim.metadata import Metadata, filename_convention, fill_item_assets

logger = logging.getLogger(__name__)


def create_collection() -> Collection:
    """Create a STAC Collection

    See `the STAC specification
    <https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md>`_
    for information about collection fields, and
    `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_
    for information about the PySTAC class.

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
            "https://stac-extensions.github.io/alternate-assets/v1.1.0/schema.json",
        ],
        keywords=c.NISAR_SIM_KEYWORDS,
    )

    collection.add_links(c.NISAR_SIM_LINKS)

    collection_assets = ItemAssetsExtension.ext(collection, add_if_missing=True)
    collection_assets.item_assets = (
        fill_item_assets()
    )  # TODO: Pass Collection ID to grab specific assets

    return collection


def create_item(source: str) -> Item:
    """Create a STAC Item

    See `the STAC specification
    <https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md>`_
    for information about an item's fields, and
    `Item<https://pystac.readthedocs.io/en/latest/api/pystac.html#pystac.Item>`_ for
    information on the PySTAC class.

    Args:
        source (str): An HREF data directory pointing to a flight

    Returns:
        Item: STAC Item object
    """
    _metadata = Metadata(source)
    prod_info = filename_convention(source)

    item = Item(
        id=_metadata.id,
        properties={},
        geometry=_metadata.geometry,
        bbox=_metadata.bbox,
        datetime=None,
        start_datetime=prod_info["start_datetime"],
        end_datetime=prod_info["end_datetime"],
        stac_extensions=[
            "https://stac-extensions.github.io/alternate-assets/v1.1.0/schema.json",
        ],
    )

    item.add_asset(
        prod_info["type"],
        Asset(
            title=prod_info["title"],
            media_type=MediaType.HDF5,
            description=prod_info["description"],
            roles=["data"],
            href=source,
            extra_fields={
                "alternate": {
                    "href": (
                        c.NISAR_S3_LOCATION
                        + (
                            "L0B" + source.split("L0B", 1)[-1]
                            if "RRSD" in source
                            else prod_info["type"]
                            + source.split(prod_info["type"], 1)[-1]
                        )
                    )
                },
            },
        ),
    )
    proj_attrs = ProjectionExtension.ext(item, add_if_missing=True)
    proj_attrs.epsg = c.NISAR_SIM_EPSG

    sat = SatExtension.ext(item, add_if_missing=True)
    # sat.absolute_orbit = _metadata.absolute_orbit # TODO: current value zero
    sat.orbit_state = prod_info["orbit_state"]

    return item
