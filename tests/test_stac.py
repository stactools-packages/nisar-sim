from stactools.nisar_sim import stac

from . import test_data


def test_create_collection() -> None:
    # Write tests for each for the creation of a STAC Collection
    # Create the STAC Collection...

    collection = stac.create_collection()
    collection.set_self_href(None)
    assert collection.id == "nisar-sim"
    collection.validate()


def test_create_item() -> None:
    # Write tests for each for the creation of STAC Items
    # Create the STAC Item...
    item = stac.create_item(
        test_data.get_path(
            "data/L0B/ALOS1_Rosamond_20081012/NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001.h5"
        )
    )

    # Check that it has some required attributes
    assert (
        item.id
        == "NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001"
    )
    assert item.geometry is not None
    assert item.bbox is not None

    item.validate()
