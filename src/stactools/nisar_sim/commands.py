import logging

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
    def create_item_command(source: str, destination: str, dither: str) -> None:
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Item
        """
        item = stac.create_item(source, dither)

        item.save_object(dest_href=destination)

        return None

    return nisarsim
