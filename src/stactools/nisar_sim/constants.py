from datetime import datetime
from typing import Optional

from pystac import Extent, Link, Provider
from pystac import ProviderRole as PR
from pystac import SpatialExtent, TemporalExtent
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
NISAR_SIM_DESCRIPTION = "Simulated NISAR products are specialized UAVSAR PolSAR products. They include files described in the UAVSAR PolSAR Data Format but with different number of MLC looks and GRD grid; as well as additional NISAR RSLC HDF5 files, radiometric terrain correction layer, and flat earth incidence angle files."  # noqa

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

NMODE = ["129", "138", "143"]  # center frequency, bandwidth, and polarization
XTALK = ["X", "C"]
