# Convenience commands for the Quantum Water Optimizer.
# These are shortcuts only and do not change project behavior.

.PHONY: help install run lint clean

help:
	@echo "Available targets:"
	@echo "  install  Install Python dependencies from requirements.txt"
	@echo "  run      Run the main application"
	@echo "  lint     Compile-check all Python sources"
	@echo "  clean    Remove Python cache files"

install:
	pip install -r requirements.txt

run:
	python main.py

lint:
	python -m compileall -q .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
