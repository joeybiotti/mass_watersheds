.PHONY: all ingest validate overlay test clean format lint

# Run the entire pipeline
all: ingest validate overlay

# Ingestion steps
ingest:
	python -m scripts.ingestion.ingest_municipal_boundaries
	python -m scripts.ingestion.ingest_watersheds

# Validation steps
validate:
	python -m scripts.validation.validate_municipal_boundaries
	python -m scripts.validation.validate_watersheds

# Overlay step
overlay:
	python -m scripts.overlays.clip_watersheds_to_municipalities

# Run visualization
viz:
	python -m scripts.viz.generate_folium_map

# Run tests
test:
	pytest -q

# Format code
format:
	ruff format .
	ruff check --fix .

# Lint code
lint:
	ruff check .
	ruff format --check .

# Clean generated data and outputs
clean:
	rm -rf data/clean/*
	rm -rf data/validated/*
	rm -rf data/enriched/*
	rm -rf output/*