import h5py
import pytest


@pytest.fixture(scope="session")  # type: ignore
def mock_h5_file(tmp_path_factory: pytest.TempPathFactory) -> str:
    path = (
        tmp_path_factory.getbasetemp()
        / "NISAR_L0_PR_RRSD_001_005_A_128S_20081012T060910_20081012T060926_P01101_F_J_001.h5"
    )

    with h5py.File(path, "w") as f:
        science_group = f.create_group("science")
        lsar_group = science_group.create_group("LSAR")
        identification_group = lsar_group.create_group("identification")

        bounding_polygon_data = b"POLYGON ((-118.249180075257 34.2477830839722 0,-118.153410411349 34.2641142582268 0,-118.274189005355 34.3464716173865 0,-118.249180075257 34.2477830839722 0))"
        identification_group.create_dataset(
            "boundingPolygon", data=bounding_polygon_data
        )

    return str(path)
