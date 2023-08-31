from stactools.nisar_sim import stac


def test_create_collection() -> None:
    # Write tests for each for the creation of a STAC Collection
    # Create the STAC Collection...
    collection = stac.create_collection()
    collection.set_self_href("")

    # Check that it has some required attributes
    assert collection.id == "nisar-sim"
    # self.assertEqual(collection.other_attr...

    # Validate
    collection.validate()


def test_create_item(example_href: str) -> None:
    # Write tests for each for the creation of STAC Items
    # Create the STAC Item...
    item = stac.create_item(
        example_href,
        dither="X",
        nmode="129",
    )

    # Check that it has some required attributes
    assert item.id == "winnip_31604_12061_004_120717_L090_CX_07"
    # self.assertEqual(item.other_attr...

    # Validate
    item.validate()
