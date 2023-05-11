from typing import Dict, Optional

from pystac import MediaType
from pystac.extensions.item_assets import AssetDefinition

from stactools.nisar_sim import constants as c


def NISAR_SIM_ASSETS_NO_DITHER(
    xtalk: str, frequency: str
) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}X_{frequency}.ann": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Annotation File",
                "type": MediaType.TEXT,
                "description": f"No Dither: {frequency} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HH_{xtalk}X_{frequency}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HH Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for HH polarization",
                "role": ["data"],
            }
        ),
        f"HV_{xtalk}X_{frequency}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HV Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for HV polarization",
                "role": ["data"],
            }
        ),
        f"VH_{xtalk}X_{frequency}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} VH Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for VH polarization",
                "role": ["data"],
            }
        ),
        f"VV_{xtalk}X_{frequency}.slc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} VV Polarization Single Look Complex File",
                "type": "application/octet-stream",
                "description": "Single look complex slant range image for VV polarization",
                "role": ["data"],
            }
        ),
        f"HHHH_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HHHH Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHHH",
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HVHV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HVHV",
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} VVVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct VVVV",
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HHHV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHHV",
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HHVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HHVV",
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}X_{frequency}.mlc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HVVV Crossproduct Multi Look File",
                "type": "application/octet-stream",
                "description": "Multi look cross product slant range image for crossproduct HVVV",
                "role": ["data"],
            }
        ),
        f"HHHH_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}X_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"No Dither: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.hgt": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} HGT File",
                "type": "application/octet-stream",
                "description": (
                    "Digital elevation model (DEM) used during processing and ground projection"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.inc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Incidence Angle File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range local incidence angle, the angle between"
                    " the surface normal and the radar line of sight."
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.flat.inc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Flat Earth Incidence Angle File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range local incidence angle, the angle between"
                    " the surface normal and the radar line of sight"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.slope": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Terrain Slope File",
                "type": "application/octet-stream",
                "description": (
                    "Ground range terrain slope containing the derivatives of the DEM in the East"
                    " and North direction, used to compute the local incidence angle"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.rtc": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Radiometric Terrain Correction Factor",
                "type": "application/octet-stream",
                "description": (
                    "Radiometric terrain correction factor that can be applied to grd files"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}X_{frequency}.kmz": AssetDefinition(
            {
                "title": f"{xtalk}X_{frequency} Keyhole Markup Language Zipped File",
                "type": "application/vnd.google-earth.kmz",
                "description": (
                    "Full resolution image representing the GRD data in Keyhole Markup Language"
                ),
                "role": ["overlay"],
            }
        ),
        f"{xtalk}X_{frequency[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": f"No Dither: {frequency[:-1]} Frequency HDF5 file in NISAR format",
                "role": ["data"],
            }
        ),
    }


def NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(
    xtalk: str, frequency: str
) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}G_{frequency}.ann": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Annotation File",
                "type": MediaType.TEXT,
                "description": f"Dithered With Gaps: {frequency} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HHHH_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}G_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}G_{frequency} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered With Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}G_{frequency[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": (
                    f"Dithered With Gaps: {frequency[:-1]} Frequency HDF5 file in NISAR format"
                ),
                "role": ["data"],
            }
        ),
    }


def NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(
    xtalk: str, frequency: str
) -> Dict[str, AssetDefinition]:
    return {
        f"{xtalk}D_{frequency}.ann": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Annotation File",
                "type": MediaType.TEXT,
                "description": f"Dithered Without Gaps: {frequency} Annotation File",
                "role": ["metadata"],
            }
        ),
        f"HHHH_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct HHHH",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHH"
                ),
                "role": ["data"],
            }
        ),
        f"HVHV_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct HVHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVHV"
                ),
                "role": ["data"],
            }
        ),
        f"VVVV_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct VVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct VVVV"
                ),
                "role": ["data"],
            }
        ),
        f"HHHV_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct HHHV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHHV"
                ),
                "role": ["data"],
            }
        ),
        f"HHVV_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct HHVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HHVV"
                ),
                "role": ["data"],
            }
        ),
        f"HVVV_{xtalk}D_{frequency}.grd": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency} Ground Range Projected File for Crossproduct HVVV",
                "type": "application/octet-stream",
                "description": (
                    f"Dithered Without Gaps: {frequency} ground range projected (equiangular) and"
                    " multi-looked data for crossproduct HVVV"
                ),
                "role": ["data"],
            }
        ),
        f"{xtalk}D_{frequency[:-1]}.h5": AssetDefinition(
            {
                "title": f"{xtalk}D_{frequency[:-1]} HDF5 Data File",
                "type": MediaType.HDF5,
                "description": (
                    f"Dithered Without Gaps: {frequency[:-1]} Frequency HDF5 file in NISAR format"
                ),
                "role": ["data"],
            }
        ),
    }


def get_assets(
    collection: Optional[bool] = None,
    dither: Optional[str] = None,
    xtalk: Optional[str] = None,
    frequency: Optional[str] = None,
) -> Dict[str, AssetDefinition]:
    all_frequencies = [f"{freq}{suffix}" for freq in c.NMODE for suffix in ["A", "B"]]
    assets = {}

    if collection:
        for _talk in c.XTALK:
            for _frequency in all_frequencies:
                assets.update(NISAR_SIM_ASSETS_NO_DITHER(_talk, _frequency))
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(_talk, _frequency))
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(_talk, _frequency))
    if dither:
        if not xtalk:
            xtalk = "C"
        for _frequency in all_frequencies:
            if dither == "X":
                assets.update(NISAR_SIM_ASSETS_NO_DITHER(xtalk, _frequency))
            if dither == "G":
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITH_GAPS(xtalk, _frequency))
            if dither == "D":
                assets.update(NISAR_SIM_ASSETS_DITHERED_WITHOUT_GAPS(xtalk, _frequency))

    return assets
