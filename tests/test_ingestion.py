from pathlib import Path

import geopandas as gpd

from scripts.ingestion.ingest_municipal_boundaries import fetch_municipal_boundaries
from scripts.ingestion.ingest_watersheds import fetch_watersheds

FIXTURE_DIR = Path(__file__).parent / "fixtures"
MUNI_FIXTURE = FIXTURE_DIR / "muni_sample.geojson"
WATER_FIXTURE = FIXTURE_DIR / "water_sample.geojson"


def test_ingest_municipal_boundaries_loads_gdf():
    gdf = gpd.read_file(MUNI_FIXTURE)

    assert isinstance(gdf, gpd.GeoDataFrame)
    assert not gdf.empty
    assert "geometry" in gdf.columns
    assert gdf.crs.to_epsg() == 4326
    assert "TOWN" in gdf.columns


def test_ingest_watersheds_loads_gdf():
    gdf = gpd.read_file(WATER_FIXTURE)

    assert isinstance(gdf, gpd.GeoDataFrame)
    assert not gdf.empty
    assert "geometry" in gdf.columns
    assert gdf.crs.to_epsg() == 4326
    assert "WATERSHED" in gdf.columns


def test_ingestion_functions_accept_paths():
    muni_gdf = fetch_municipal_boundaries(MUNI_FIXTURE)
    water_gdf = fetch_watersheds(WATER_FIXTURE)

    assert isinstance(muni_gdf, gpd.GeoDataFrame)
    assert isinstance(water_gdf, gpd.GeoDataFrame)
    assert not muni_gdf.empty
    assert not water_gdf.empty
