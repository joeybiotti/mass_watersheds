.PHONY: all ingest validate overlay enriched test clean

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

# Run main orchestrator
run:
	python -m main

# Run tests
test:
	pytest -q

# Clean generated data
clean:
	rm -rf data/clean/*
	rm -rf data/validated/*
	rm -rf data/enriched/*
