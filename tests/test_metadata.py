from stactools.nisar_sim import metadata


def test_MetadataLinks() -> None:
    href = (
        "https://downloaduav.jpl.nasa.gov/Release2e/"
        "Haywrd_14501_08037_007_080729_L090_CX_01/"
    )
    metalinks = metadata.MetadataLinks(href=href, dither="X", nmode="X")
    assert (
        metalinks.h5_href == "https://downloaduav.jpl.nasa.gov/Release2e/"
        "Haywrd_14501_08037_007_080729_L090_CX_01/Haywrd_14501_08037_007_080729_L090_CX_X_01.h5"
    )
