from stactools.nisar_sim import stac


def test_create_collection() -> None:
    """Test the creation of a STAC Collection."""
    collection = stac.create_collection()
    collection.set_self_href(None)
    assert collection.id == "nisar-sim"
    collection.validate()


def test_create_item(mock_h5_file: str) -> None:
    """Test the creation of a STAC Item."""
    item = stac.create_item(mock_h5_file)

    # Checking that it has some required attributes
    assert (
        item.id
        == "NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001"
    )
    assert item.geometry is not None
    assert item.bbox is not None
    item.validate()
