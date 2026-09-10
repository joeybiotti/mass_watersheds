from pathlib import Path

import geopandas as gpd

# [Overlay tests](ca://s?q=Write_overlay_tests)


def test_overlay_output_exists():
    assert Path("data/enriched/watersheds_by_municipality.geojson").exists()


def test_overlay_has_results():
    gdf = gpd.read_file("data/enriched/watersheds_by_municipality.geojson")
    assert len(gdf) > 0


def test_overlay_crs_is_4326():
    gdf = gpd.read_file("data/enriched/watersheds_by_municipality.geojson")
    assert gdf.crs.to_epsg() == 4326
