# Amazon Bestselling Books Analysis

A beginner Python project exploring Amazon bestselling book entries from 2009 to 2019. It includes a command-line analysis script and an interactive Streamlit dashboard.

## What the project explores

- Number of book entries by genre
- Average rating and price by genre
- Authors with the most entries
- Average rating and price by year
- Books rated 4.9 or higher
- How average book prices change by year

## Tools used

- Python
- pandas
- Matplotlib
- Streamlit

## Project structure

```text
amazon-book-dashboard/
├── app.py
├── analyse.py
├── requirements.txt
├── README.md
└── data/
    └── books.csv
```

## Set up and run

Open a terminal in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the analysis script:

```powershell
python analyse.py
```

Start the interactive dashboard:

```powershell
python -m streamlit run app.py
```

Streamlit will show a local web address in the terminal. Open that address in a browser to use the dashboard.

## Dataset

The CSV contains 550 book entries and these columns:

`Name`, `Author`, `User Rating`, `Reviews`, `Price`, `Year`, and `Genre`.

Place the file at `data/books.csv` before running the scripts. Add the dataset’s download source here: **[insert source link]**.

## Data limitation

The dataset does not include sales counts. This project analyzes entries on the bestseller list, ratings, reviews, prices, and genres; it cannot determine how many copies a book sold. A book may appear in multiple years, so entry counts represent appearances in the dataset.

## Learning goals

This project practices loading CSV files, inspecting and cleaning data, handling duplicates, filtering and grouping with pandas, calculating summaries, and creating charts.
