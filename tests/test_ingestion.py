from pathlib import Path

import geopandas as gpd

# [Ingestion tests](ca://s?q=Write_ingestion_tests)


def test_ingestion_outputs_exist():
    assert Path("data/clean/municipalities_clean.geojson").exists()
    assert Path("data/clean/watersheds_clean.geojson").exists()


def test_ingestion_crs_is_4326():
    muni = gpd.read_file("data/clean/municipalities_clean.geojson")
    ws = gpd.read_file("data/clean/watersheds_clean.geojson")

    assert muni.crs.to_epsg() == 4326
    assert ws.crs.to_epsg() == 4326
