from typing import Dict, Optional

from pystac import MediaType
from pystac.extensions.item_assets import AssetDefinition

from stactools.nisar_sim import constants as c


def NISAR_SIM_ASSETS_NO_DITHER(xtalk: str, nmode: str) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}X_{nmode}.ann": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Annotation File",
                "type": MediaType.TEXT,
                "description": f"No Dither: {nmode} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HH_{xtalk}X_{nmode}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HH Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for HH polarization",
                "role": ["data"],
            }
        ),
        f"HV_{xtalk}X_{nmode}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HV Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for HV polarization",
                "role": ["data"],
            }
        ),
        f"VH_{xtalk}X_{nmode}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} VH Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for VH polarization",
                "role": ["data"],
            }
        ),
        f"VV_{xtalk}X_{nmode}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} VV Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for VV polarization",
                "role": ["data"],
            }
        ),
        f"HHHH_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HHHH Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHHH",
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HVHV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HVHV",
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} VVVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct VVVV",
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HHHV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHHV",
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HHVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHVV",
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}X_{nmode}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HVVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HVVV",
                "role": ["data"],
            }
        ),
        f"HHHH_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}X_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.hgt": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} HGT File",
                "type": "application/octet-stream",
                "description": (
                    "Digital elevation model (DEM) used during processing and ground projection"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.inc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Incidence Angle File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range local incidence angle, the angle between"
                    " the surface normal and the radar line of sight."
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.flat.inc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Flat Earth Incidence Angle File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range local incidence angle, the angle between"
                    " the surface normal and the radar line of sight"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.slope": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Terrain Slope File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range terrain slope containing the derivatives of the DEM in the East"
                    " and North direction, used to compute the local incidence angle"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.rtc": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Radiometric Terrain Correction Factor",
                "type": "application/octet-stream",
                "description": (
                    "Radiometric terrain correction factor that can be applied to grd files"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{nmode}.kmz": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode} Keyhole Markup Language Zipped File",
                "type": "application/vnd.google-earth.kmz",
                "description": (
                    "Full resolution image representing the GRD data in Keyhole Markup Language"
                ),
                "role": ["overlay"],
            }
        ),
        f"{xtalk}X_{nmode[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}X_{nmode[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": f"No Dither: {nmode[:-1]} NMode HDF5 file in NISAR format",
                "role": ["data"],
            }
        ),
    }


def NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(
    xtalk: str, nmode: str
) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}G_{nmode}.ann": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Annotation File",
                "type": MediaType.TEXT,
                "description": f"Dithered With Gaps: {nmode} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HHHH_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}G_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}G_{nmode[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}G_{nmode[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": (
                    f"Dithered With Gaps: {nmode[:-1]} NMode HDF5 file in NISAR format"
                ),
                "role": ["data"],
            }
        ),
    }


def NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(
    xtalk: str, nmode: str
) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}D_{nmode}.ann": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Annotation File",
                "type": MediaType.TEXT,
                "description": f"Dithered Without Gaps: {nmode} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HHHH_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}D_{nmode}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {nmode} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}D_{nmode[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}D_{nmode[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": (
                    f"Dithered Without Gaps: {nmode[:-1]} NMode HDF5 file in NISAR format"
                ),
                "role": ["data"],
            }
        ),
    }


def get_assets(
    collection: Optional[bool] = None,
    dither: Optional[str] = None,
    xtalk: Optional[str] = None,
) -> Dict[str, AssetDefinition]:
    nmodes = [f"{mode}{nmode}" for mode in c.NMODE for nmode in ["A", "B"]]
    assets = {}

    if collection:
        for _talk in c.XTALK:
            for _nmode in nmodes:
                assets.update(NISAR_SIM_ASSETS_NO_DITHER(_talk, _nmode))
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(_talk, _nmode))
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(_talk, _nmode))
    if dither:
        if not xtalk:
            xtalk = "C"
        for _nmode in nmodes:
            if dither == "X":
                assets.update(NISAR_SIM_ASSETS_NO_DITHER(xtalk, _nmode))
            if dither == "G":
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(xtalk, _nmode))
            if dither == "D":
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(xtalk, _nmode))

    return assets
