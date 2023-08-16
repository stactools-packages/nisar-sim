import logging
import os

import click
from click import Command, Group

from stactools.nisar_sim import stac

logger = logging.getLogger(__name__)


def create_nisarsim_command(cli: Group) -> Command:
    """Creates the stactools-nisar-sim command line utility."""

    @cli.group(
        "nisarsim",
        short_help=("Commands for working with stactools-nisar-sim"),
    )
    def nisarsim() -> None:
        pass

    @nisarsim.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str) -> None:
        """Creates a STAC Collection

        Args:
            destination (str): An HREF for the Collection JSON
        """
        collection = stac.create_collection()

        collection.set_self_href(destination)

        collection.save_object()

        return None

    @nisarsim.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    @click.option(
        "--dither",
        default="X",
        type=click.Choice(["X", "G", "D"], case_sensitive=False),
        help="single character indicating the item's dither type ('X','G','D')",
    )
    @click.option(
        "--nmode",
        default="129",
        type=click.Choice(["129", "138", "143"]),
        help="set of numbers indicating the item's nmode ('129','138','143')",
    )
    @click.option(
        "--sat-extension",
        default=False,
        type=bool,
        help="Whether to include the SAT extension. Requires that the HDF5 file is present in `product_path`.",
    )
    def create_item_command(
        source: str, destination: str, dither: str, nmode: str, sat_extension: bool
    ) -> None:
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Item
            dither (str): single character indicating the item's dither type ("X","G","D")
            nmode (str): set of numbers associated with a specific center frequency,
                bandwidth, and polarization ("129","138","143")
        """
        item = stac.create_item(source, dither, nmode)
        json_file = os.path.basename(source)
        json_path = os.path.join(destination, f"{json_file}.json")
        item.set_self_href(os.path.basename(json_path))

        item.validate()

        item.save_object(dest_href=destination)

        return None

    return nisarsim
