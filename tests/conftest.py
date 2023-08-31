import pytest

from stactools.nisar_sim.constants import NISAR_SIM_EXAMPLE_HREF


@pytest.fixture
def example_href() -> str:
    return NISAR_SIM_EXAMPLE_HREF
