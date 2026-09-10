from pathlib import Path

import geopandas as gpd


def main():
    shp = Path("data/raw/TOWNSSURVEY_POLY.shp")
    out = Path("data/raw/municipalities.geojson")

    gdf = gpd.read_file(shp)
    out.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(out, driver="GeoJSON")
    print(f"Saved municipal boundaries to {out}")


if __name__ == "__main__":
    main()
