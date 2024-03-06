from pathlib import Path

from click import Group
from click.testing import CliRunner
from pystac import Collection, Item
from stactools.nisar_sim.commands import create_nisarsim_command

command = create_nisarsim_command(Group())


def test_create_collection(tmp_path: Path) -> None:
    path = str(tmp_path / "collection.json")
    runner = CliRunner()
    result = runner.invoke(command, ["create-collection", path])
    assert result.exit_code == 0, "\n{}".format(result.output)
    collection = Collection.from_file(path)
    collection.validate()


def test_create_item(tmp_path: Path, mock_h5_file: str) -> None:
    path = str(tmp_path / "examples")
    runner = CliRunner()
    result = runner.invoke(command, ["create-item", mock_h5_file, path])
    assert result.exit_code == 0, f"\n{result.output}"
    item = Item.from_file(path)
    item.validate()
