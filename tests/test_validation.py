from pathlib import Path

import geopandas as gpd

from scripts.validation.validate_municipal_boundaries import (
    validate_municipal_boundaries,
)
from scripts.validation.validate_watersheds import validate_watersheds

FIXTURE_DIR = Path(__file__).parent / "fixtures"
MUNI_FIXTURE = FIXTURE_DIR / "muni_sample.geojson"
WATER_FIXTURE = FIXTURE_DIR / "water_sample.geojson"


def test_validate_municipal_boundaries():
    gdf = gpd.read_file(MUNI_FIXTURE)
    validated = validate_municipal_boundaries(gdf)

    assert not validated.empty
    assert validated.crs.to_epsg() == 4326
    assert validated.geometry.is_valid.all()
    assert "TOWN" in validated.columns
    assert validated.geometry.notnull().all()


def test_validate_watersheds():
    gdf = gpd.read_file(WATER_FIXTURE)
    validated = validate_watersheds(gdf)

    assert not validated.empty
    assert validated.crs.to_epsg() == 4326
    assert validated.geometry.is_valid.all()
    assert "WATERSHED" in validated.columns
    assert validated.geometry.notnull().all()
