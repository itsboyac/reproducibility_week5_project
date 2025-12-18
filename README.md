# Reproducible Book Scraping & Classification Pipeline

This project demonstrates a fully reproducible end-to-end data pipeline using Python and Make. It is designed to run in a Linux environment (specifically **WSL** on Windows) to ensure consistent behavior across different machines.

The pipeline automates data ingestion, scraping, cleaning, storage (SQLite), and machine learning classification.

---

## 📂 Project Structure

```text
reproducibility_week5_project/
├── data/
│   ├── raw/            # Raw HTML snapshots (timestamped)
│   ├── processed/      # Cleaned CSV datasets
│   └── books.db        # SQLite database for reliable storage
├── logs/               # Model training metrics (accuracy scores)
├── src/                # Python source scripts
│   ├── fetch_data.py   # Step 1: Downloads raw HTML
│   ├── scrape_books.py # Step 2: Extracts data to CSV
│   ├── clean_books.py  # Step 3: Cleans text & saves to SQLite
│   └── classify.py     # Step 4: Trains ML model
├── Makefile            # Automation tool to run pipeline steps
├── pyproject.toml      # Project configuration & dependencies, not used in this project, you can opt either this or requirements.txt
├── requirements.txt    # Pinned dependencies for reproducibility
└── README.md           # Project documentation
```

---

## 🛠️ Environment Setup (WSL & Virtual Environment)

This project requires **WSL (Windows Subsystem for Linux)** to use standard Linux automation tools like `make`.

### 1. Prerequisites

Ensure you have the following installed in your WSL terminal:

- **Python 3.10+**
- **Make** (`sudo apt install make`)

### 2. Setting up the Virtual Environment

To ensure reproducibility, we use a local virtual environment. This isolates our dependencies from the system Python.

```bash
# 1. Create the virtual environment in the project root
python3 -m venv .venv

# 2. Activate the environment (Linux/WSL command)
source .venv/bin/activate

# 3. Install dependencies
pip install requests beautifulsoup4 pandas scikit-learn

# 4. Freeze dependencies to lock versions
pip freeze > requirements.txt
```

---

## 🚀 The Pipeline (Makefile)

We use a **Makefile** to orchestrate the scripts. Each script performs one specific task, passing data to the next stage.

### How the Data Flows:

1. **Ingestion**: Downloads HTML files from the web → `data/raw/`
2. **Scraping**: Parses HTML → `data/processed/books.csv`
3. **Storage**: Cleans text and saves to SQLite (`data/books.db`) for robust querying
4. **Analysis**: Loads data from DB/CSV and outputs metrics → `logs/metrics.csv`

### Running the Pipeline

You can run individual steps or the entire pipeline at once using `make`.

| Task    | Command        | Description                                              |
|---------|----------------|----------------------------------------------------------|
| Ingest  | `make get-data`| Runs `src/fetch_data.py`. Downloads raw HTML pages.      |
| Scrape  | `make scrape`  | Runs `src/scrape_books.py`. Extracts titles/genres to CSV.|
| Clean   | `make clean`   | Runs `src/clean_books.py`. Sanitizes text and saves to SQLite.|
| Train   | `make train`   | Runs `src/classify.py`. Trains a model and logs accuracy.|
| **All** | `make all`     | **Recommended.** Runs all steps in the correct order.    |

To reproduce the entire analysis from scratch, simply run:

```bash
make all
```

---

## 📊 Data Storage Details

### Raw Data (`data/raw/`)
We save raw HTML with timestamps (e.g., `mystery-20231025.html`) to prevent overloading the server and to allow offline development.

### SQLite Database (`data/books.db`)
The cleaning script migrates data from CSV to a local SQL database. This simulates a production environment where data is queried rather than read from flat files.


