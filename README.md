# Noon 3K Products Extractor by Selenium


A Python-based data extraction script built with Selenium to scrape product listings from [Noon.com](https://www.noon.com/).
The tool automates the process of collecting product data for a given keyword, handling pagination, sorting results by highest rating, and exporting the output to a structured CSV file.

## Features

* Extracts **up to 1000 products** per keyword from Noon.com
* Filters and **sorts products by rating** (highest-rated first)
* Handles **pagination automatically**
* **Saves data to a CSV file** (ready for Excel or Google Sheets)
* Easy to run, even for non-technical users

## Extracted Data Includes

* Product Name
* Price
* Discount (if available)
* Rating
* Direct Product Link

## Use Case Examples

* Market research and competitor analysis
* Product tracking for eCommerce sellers
* Building datasets for machine learning models
* Generating CSV lists for clients or inventory systems

## Requirements

* Python 3.7+
* Google Chrome browser
* Libraries: `selenium`, `bs4`, `webdriver_manager`

Install dependencies via:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

## How to Use

1. Run the script
2. Enter your keyword when prompted (e.g., `smart watch`)
3. The script will collect up to 1000 results, sorted by rating
4. Output will be saved as a CSV on your desktop

## Notes

* This script uses `Selenium` with ChromeDriver (automatically managed by `webdriver-manager`)
* Designed for the **Egypt region** of Noon.com
* Works best with stable internet and a recent version of Chrome

## License

This project is for educational and portfolio use only. Use responsibly and respect the target website’s Terms of Service.
