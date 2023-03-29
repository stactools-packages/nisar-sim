#!/usr/bin/env python3
"""
Generate example STAC from test data
"""
import shutil
from pathlib import Path

import pystac

from stactools.nisar_sim import stac

root = Path(__file__).parents[1]
examples = root / "examples"
nisar_sim_data = root / "tests" / "data-files"

shutil.rmtree(examples, ignore_errors=True)

stac_collection = stac.create_collection()

item1 = stac.create_item(
    str(nisar_sim_data / "winnip_31604_12061_004_120717_L090_CX_07/"), dither="X"
)

stac_collection.add_items([item1])

stac_collection.normalize_hrefs(str(examples))
stac_collection.make_all_asset_hrefs_relative()
stac_collection.validate_all()
stac_collection.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)
