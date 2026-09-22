from pathlib import Path

import geopandas as gpd

from scripts.overlays.clip_watersheds_to_municipalities import (
    clip_watersheds_to_municipalities,
)

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def test_overlay_returns_geodataframe():
    muni = gpd.read_file(FIXTURE_DIR / "muni_sample.geojson")

    water = gpd.read_file(FIXTURE_DIR / "water_sample.geojson")

    result = clip_watersheds_to_municipalities(
        water,
        muni,
    )

    assert isinstance(result, gpd.GeoDataFrame)


def test_overlay_has_results():
    muni = gpd.read_file(FIXTURE_DIR / "muni_sample.geojson")

    water = gpd.read_file(FIXTURE_DIR / "water_sample.geojson")

    result = clip_watersheds_to_municipalities(
        water,
        muni,
    )

    assert not result.empty


def test_overlay_geometries_are_valid():
    muni = gpd.read_file(FIXTURE_DIR / "muni_sample.geojson")

    water = gpd.read_file(FIXTURE_DIR / "water_sample.geojson")

    result = clip_watersheds_to_municipalities(
        water,
        muni,
    )

    assert result.geometry.is_valid.all()
