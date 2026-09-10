from pathlib import Path

import geopandas as gpd


def validate_watershed():
    src = Path("data/clean/watersheds_clean.geojson")
    dst = Path("data/validated/watersheds.geojson")

    gdf = gpd.read_file(src)

    invalid_before = ~gdf.geometry.is_valid
    gdf.loc[invalid_before, "geometry"] = gdf.loc[invalid_before].buffer(0)
    invalid_after = ~gdf.geometry.is_valid

    print(f"Invalid before fix: {invalid_before.sum()}")
    print(f"Invalid after fix: {invalid_after.sum()}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(dst, driver="GeoJSON")


if __name__ == "__main__":
    validate_watershed()
