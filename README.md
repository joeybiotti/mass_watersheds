# Mass Watersheds

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![GeoPandas](https://img.shields.io/badge/GeoPandas-Geospatial-green.svg)
![DuckDB](https://img.shields.io/badge/DuckDB-Analytics-yellow.svg)
![Folium](https://img.shields.io/badge/Folium-Interactive%20Maps-lightgrey.svg)
![License](https://img.shields.io/badge/License-Open-lightblue.svg)

**Mass Watersheds** is a geospatial and hydrology-focused project that maps Massachusetts reservoir levels, watershed boundaries, drought indicators, and related environmental data. It combines GIS datasets with time-series water data to create an interactive, data-driven view of water conditions across the state.

## Overview

Mass Watersheds integrates:

* Reservoir polygons and watershed boundaries
* Time-series reservoir level data
* Drought severity indicators
* Spatial analysis using GeoPandas
* Interactive mapping using Folium
* Local analytics using DuckDB

The project is designed to be lightweight, modular, and easy to extend as new datasets or visualizations are added.

## Features

* **GIS Data Processing:** Load and process GeoJSON, shapefiles, and GeoPackage formats.
* **Data Ingestion:** Ingest hydrology time-series data from public sources.
* **Spatial Visualizations:** Color-code reservoirs based on percent-full status or drought severity.
* **Interactive Maps:** Render interactive Folium maps with custom layers and informative popups.
* **Clean Workflow:** Maintain a reproducible, modular Python analytics pipeline.

## Project Structure

```text
mass_watersheds/
  README.md
  .gitignore
  main.py
  app/
    __init__.py
  data_raw/
    .gitkeep
  notebooks/
    .gitkeep
  scripts/
    __init__.py
  requirements.txt
```

## Quickstart

### Prerequisites

* Python 3.10+

### Setup & Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the project:
   ```bash
   python main.py
   ```

## Goals

* Provide a clear visual understanding of Massachusetts water conditions.
* Build a modular GIS + hydrology analytics pipeline.
* Support future expansion into drought forecasting and watershed modeling.

## License

This project is open for personal and educational use.