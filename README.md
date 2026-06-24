# Nairobi Real Estate Scraper 2025

An automated tool to track and analyze rental market trends across Nairobi's residential estates. It identifies "undervalued" zones by comparing local estate averages against city-wide benchmarks for specific bedroom counts.

## Features
- Web scraping logic for Nairobi property portals.
- Comparative analysis of price-per-bedroom.
- Anomaly detection for undervalued listings.
- Data visualization (Seaborn/Matplotlib).

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python scraper.py
```

## Output
- `nairobi_rentals_2025.csv`: Raw dataset.
- `nairobi_market_trends.png`: Visual distribution of prices per estate.

## Disclaimer
This tool is for educational purposes. Ensure compliance with the Terms of Service of any website you scrape using `robots.txt` checks.