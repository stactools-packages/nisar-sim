import os.path
from tempfile import TemporaryDirectory
from typing import Callable, List

import pystac
from click import Command, Group
from click.testing import CliRunner
from stactools.cli.cli import cli

from stactools.nisar_sim.commands import create_nisarsim_command


class CommandsTest:
    def __init__(self) -> None:
        self.runner = CliRunner()

    def create_subcommand_functions(self) -> List[Callable[[Group], Command]]:
        return [create_nisarsim_command]

    def test_create_collection(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-collection command and validate

            # Example:
            destination = os.path.join(tmp_dir, "collection.json")

            result = self.runner.invoke(
                cli, ["nisarsim", "create-collection" f"{destination}"]
            )

            assert result.exit_code == 0, f"\n{result.output}"

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            assert len(jsons) == 1

            collection = pystac.read_file(destination)
            assert collection.id == "nisar-sim"
            # assert collection.other_attr...

            collection.validate()

    def test_create_item(self, example_href: str) -> None:
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-item command and validate

            # Example:
            destination = os.path.join(tmp_dir, "item.json")
            dither = "X"
            nmode = "129"
            result = self.runner.invoke(
                cli,
                [
                    "nisarsim",
                    "create-item",
                    example_href,
                    f"{destination}",
                    f"--dither {dither}",
                    f"--nmode {nmode}",
                ],
            )
            assert result.exit_code == 0, f"\n{result.output}"

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            assert len(jsons) == 1

            item = pystac.read_file(destination)
            assert item.id == "winnip_31604_12061_004_120717_L090_CX_07"
            # assert item.other_attr...

            item.validate()
