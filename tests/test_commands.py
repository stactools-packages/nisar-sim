from pathlib import Path

from click import Group
from click.testing import CliRunner
from pystac import Collection, Item
from stactools.nisar_sim.commands import create_nisarsim_command

from . import test_data

command = create_nisarsim_command(Group())


def test_create_collection(tmp_path: Path) -> None:
    path = str(tmp_path / "collection.json")
    runner = CliRunner()
    result = runner.invoke(command, ["create-collection", path])
    assert result.exit_code == 0, "\n{}".format(result.output)
    collection = Collection.from_file(path)
    collection.validate()


def test_create_item(tmp_path: Path) -> None:
    stac_id = (
        "NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001"
    )
    asset_href = test_data.get_path(f"data/L0B/ALOS1_Rosamond_20081012/{stac_id}.h5")
    path = str(tmp_path / "examples")
    runner = CliRunner()
    result = runner.invoke(command, ["create-item", asset_href, path])
    assert result.exit_code == 0, f"\n{result.output}"
    item = Item.from_file(path)
    item.validate()
