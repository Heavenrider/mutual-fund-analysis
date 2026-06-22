# Mutual Fund Data Analysis - Day 1

## Objective

Perform data ingestion, validation, and live NAV fetching for mutual fund datasets.

## Tasks Completed

- Created project folder structure
- Loaded 10 CSV datasets
- Inspected dataset shapes, data types, and sample records
- Identified missing values and duplicate rows
- Fetched live NAV data using mfapi.in
- Retrieved NAV for 5 key schemes
- Explored fund master dataset
- Validated AMFI codes against NAV history
- Generated data quality summary

## Technologies Used

- Python
- Pandas
- NumPy
- Requests
- Jupyter
- Git

## Project Structure

mutual_fund_analysis/

data/
├── raw/
└── processed/

notebooks/

sql/

dashboard/

reports/

data_ingestion.py

live_nav_fetch.py

requirements.txt