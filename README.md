Netflix Content Trends Analysis

VOIS_AICTE_Oct2025_MajorProject_Ashok_Panuganti

Project Overview

This project analyzes a Netflix dataset (7,789 records) to understand content trends over time. The analysis focuses on:

Movies vs TV Shows growth (year-wise)
Popular genres and how they evolved
Country-wise content contributions
Key insights and strategic recommendations for content acquisition
Contents
data/ — dataset CSV (not included in repo; add Netflix Dataset (5).csv)
notebooks/ — Jupyter notebooks with EDA and visualizations
scripts/ — Python scripts to clean data and produce charts
outputs/ — generated charts and summary files (PNG, CSV, TXT)
reports/ — final PPT and project report
README.md, requirements.txt, .gitignore
How to run
Create a virtual environment:
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

Install dependencies:
pip install -r requirements.txt

Place your dataset in data/ and name it Netflix Dataset (5).csv.
Run the analysis notebook or script:
# Jupyter
jupyter notebook notebooks/Netflix_Analysis.ipynb

# or run python script
python scripts/run_analysis.py

Generated charts and outputs will appear in outputs/ for inserting into PPT.
Key Findings (summary)
Trend of Movies vs TV Shows (yearly additions) — visualized as outputs/movies_vs_tv_trend.png
Top genres (bar chart) — outputs/top_genres.png
Country contributions (bar chart) — outputs/top_countries.png
Strategic recommendations included in reports/Recommendations.md
Author

Ashok Panuganti — VOIS AICTE Major Project (Oct 2025)

License

MIT


Python

pycache/
*.py[cod]
*.pyo
.pyd
env/
venv/
venv/
.ipynb_checkpoints/

Data and outputs (do NOT commit large raw data)

data/
outputs/
reports/*.pptx
*.csv

OS / Editor

.DS_Store
Thumbs.db
.vscode/
.idea/
