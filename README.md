# 🛰️ Planet Hunter AI

A machine learning system to classify Kepler space telescope signals as real exoplanet candidates or false positives.

## 🚀 Quick Start

### 1. Setup Environment
First, clone the repo and create a virtual environment:

```bash
git clone <your-repo-url>
cd planet-hunter-ai
python -m venv venv
```

Activate the environment:

- **Windows:** `\.\venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Download Data
We use a script to fetch the latest data directly from the NASA Exoplanet Archive:

```bash
python src/data_download.py
```

## 🛠️ Project Structure

- `data/`: Local storage for the NASA CSV (git-ignored).
- `notebooks/`: Exploratory Data Analysis and model prototyping.
- `src/`: Production-ready Python scripts for cleaning and modeling.
- `app/`: Streamlit dashboard code.

## 📊 The Data

We are using the Kepler Objects of Interest (KOI) Cumulative Table.

- **Target Variable:** `koi_disposition`  
- **Goal:** Binary classification (Planet-like vs. False Positive)

---
