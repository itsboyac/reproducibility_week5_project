# Reproducibility & MLOps Project

A reproducible end-to-end Machine Learning pipeline that fetches data, trains a text classifier, and serves it via an API and Streamlit UI.

## Overview

This project demonstrates how to build a clean, reproducible MLOps workflow. It scrapes book data from [books.toscrape.com](http://books.toscrape.com), processes it, trains a Logistic Regression model to classify book genres, and deploys the model using FastAPI and Streamlit.

## Components

The pipeline is managed via `make` commands:

1.  **Fetch**: Download raw HTML data.
2.  **Scrape**: Parse HTML to extract book titles and genres.
3.  **Clean**: Clean text and store in CSV/SQLite.
4.  **Train**: Train model and save artifacts (`model.pkl`, `vectorizer.pkl`) and metrics.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Install dependencies
poetry install
```

## Usage

You can run the entire pipeline or individual steps using `make`. Ensure you are inside the `poetry` environment or prefix commands with `poetry run`.

```bash
# Run the full pipeline (Fetch -> Scrape -> Clean -> Train)
make all

# Or run individual steps:
make get-data   # Download raw HTML
make scrape     # Extract data to CSV
make clean      # Clean data & save to DB
make train      # Train model & save artifacts
```

## Running the Application

### 1. Start the API Backend
The backend runs on FastAPI.

```bash
uvicorn src.api:app --reload
```
The API will be available at `http://localhost:8000`.

### 2. Start the Frontend UI
The frontend runs on Streamlit. Open a new terminal:

```bash
streamlit run src/app.py
```
The UI will open in your browser at `http://localhost:8501`.

## Project Structure

```
├── data/           # Raw and processed data
├── logs/           # Training metrics
├── models/         # Saved model artifacts
├── src/            # Source code
│   ├── api.py      # FastAPI backend
│   ├── app.py      # Streamlit frontend
│   ├── classify.py # Model training script
│   ├── clean...    # Data processing scripts
├── Dockerfile      # Container configuration
├── Makefile        # Pipeline automation
└── pyproject.toml  # Dependencies
```
