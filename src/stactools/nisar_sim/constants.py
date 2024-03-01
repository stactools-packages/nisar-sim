from datetime import datetime
from typing import Optional

from pystac import Extent, Link, Provider, SpatialExtent, TemporalExtent
from pystac import ProviderRole as PR
from pystac.utils import str_to_datetime

NISAR_SIM_COLLECTION_START: Optional[datetime] = str_to_datetime("2008-01-01T00:00:00Z")
NISAR_SIM_TEMPORAL_EXTENT = TemporalExtent([[NISAR_SIM_COLLECTION_START, None]])
NISAR_SIM_SPATIAL_EXTENT = SpatialExtent([-180.0, -90.0, 180.0, 90.0])
NISAR_SIM_EXTENT = Extent(NISAR_SIM_SPATIAL_EXTENT, NISAR_SIM_TEMPORAL_EXTENT)

NISAR_SIM_PROVIDERS = [
    Provider(
        "NASA/JPL-Caltech",
        roles=[PR.PRODUCER, PR.PROCESSOR, PR.LICENSOR],
        url="https://www.jpl.nasa.gov/caltechjpl-privacy-policies-and-important-notices",
    ),
    Provider(
        "NASA/JPL-Caltech",
        roles=[PR.HOST],
        url="https://www.jpl.nasa.gov/caltechjpl-privacy-policies-and-important-notices",
    ),
]
NISAR_SIM_KEYWORDS = ["SAR", "NISAR", "Simulated"]
NISAR_SIM_DESCRIPTION = (
    "Simulated NISAR products are specialized UAVSAR PolSAR products. "
    "They include files described in the UAVSAR PolSAR Data Format but with different "
    "number of MLC looks and GRD grid; as well as additional NISAR RSLC HDF5 files, "
    "radiometric terrain correction layer, and flat earth incidence angle files."
)

NISAR_SIM_LINKS = [
    Link(
        rel="documentation",
        target=(
            "https://uavsar.jpl.nasa.gov/science/documents/nisar-sample-products.html"
        ),
        media_type="application/html",
        title="Simulated NISAR Products documentation",
        extra_fields={
            "description": (
                "Simulated NISAR products are generated from UAVSAR data to emulate NISAR data"
                " characteristics in order to help users test their algorithms and get a sense of"
                " the quality of future NISAR products. Click on the links below to go to the"
                " desired section."
            )
        },
    ),
    Link(
        rel="license",
        target="https://www.jpl.nasa.gov/jpl-image-use-policy",
        title="NASA/JPL-Caltech Image Use Policy",
    ),
]
NISAR_SIM_PLATFORMS = ["NISAR"]
NISAR_SIM_INSTRUMENTS = ["L-band"]
NISAR_SIM_EPSG = 4326

NISAR_S3_LOCATION = "s3://sds-n-cumulus-prod-nisar-sample-data"

NISAR_PRODUCTS = {
    "RRSD": {
        "title": "Unfocused raw SAR data",
        "description": "Level 0 Unfocused raw SAR data",
    },
    "RSLC": {
        "title": "Focused SAR image in range-doppler coordinates (zero-doppler steered)",
        "description": "Level 1 Focused SAR image in range-doppler coordinates (zero-doppler steered)",
    },
    "RIFG": {
        "title": "Phase-wrapped interferogram in range-doppler coordinates (zero-doppler steered)",
        "description": "Level 1 Phase-wrapped interferogram in range-doppler coordinates (zero-doppler steered)",
    },
    "RUNW": {
        "title": "Phase-unwrapped interferogram in range-doppler coordinates (zero-doppler steered)",
        "description": "Level 1 Phase-unwrapped interferogram in range-doppler coordinates (zero-doppler steered)",
    },
    "ROFF": {
        "title": "Pixel offsets in range-doppler coordinates (zero-doppler steered)",
        "description": "Level 1 Pixel offsets in range-doppler coordinates (zero-doppler steered)",
    },
    "GSLC": {
        "title": "Focused SAR image in geocoded coordinates",
        "description": "Level 2 Focused SAR image in geocoded coordinates",
    },
    "GUNW": {
        "title": "Phase-unwrapped interferogram in geocoded coordinates",
        "description": "Level 2 Phase-unwrapped interferogram in geocoded coordinates",
    },
    "GOFF": {
        "title": "Pixel offsets in geocoded coordinates",
        "description": "Level 2 Pixel offsets in geocoded coordinates",
    },
    "GCOV": {
        "title": "SAR covariance product in geocoded coordinates",
        "description": "Level 2 SAR covariance product in geocoded coordinates",
    },
    "SME2": {
        "title": "Global Soil Moisture Product",
        "description": "Level 3 Global Soil Moisture Product",
    },
}
