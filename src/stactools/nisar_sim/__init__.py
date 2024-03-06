import stactools.core
from stactools.cli.registry import Registry
from stactools.nisar_sim.stac import create_collection, create_item

__all__ = ["create_collection", "create_item"]

stactools.core.use_fsspec()


def register_plugin(registry: Registry) -> None:
    from stactools.nisar_sim import commands

    registry.register_subcommand(commands.create_nisarsim_command)


__version__ = "0.1.0"
