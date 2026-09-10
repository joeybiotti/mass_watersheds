import geopandas as gpd

# [Validation tests](ca://s?q=Write_validation_tests)


def test_municipal_geometries_valid():
    gdf = gpd.read_file("data/validated/municipalities.geojson")
    assert gdf.geometry.is_valid.all()


def test_watershed_geometries_valid():
    gdf = gpd.read_file("data/validated/watersheds.geojson")
    assert gdf.geometry.is_valid.all()
