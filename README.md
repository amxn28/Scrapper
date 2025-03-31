# Amazon Reviews Scraper

This Python script scrapes customer reviews from Amazon product pages and saves them to an Excel file.

## Features

- Extracts product title, review titles, ratings, and review bodies
- Handles pagination to scrape multiple pages of reviews
- Includes proxy support (though currently not implemented)
- Saves data to an Excel file for easy analysis

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

## Installation

1. Clone this repository or download the script
2. Install the required packages:
   ```
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. Set the `productUrl` variable to the Amazon product URL you want to scrape
2. Optionally configure proxy settings in the `getRandomProxy()` function
3. Run the script:
   ```
   python amazon_review_scraper.py
   ```

The script will:
- Calculate how many review pages exist
- Iterate through each page
- Extract all reviews
- Save them to an Excel file named `output.xlsx`

## Notes

- Amazon may block scraping attempts if done too aggressively
- The proxy functionality is currently just a placeholder
- You may need to adjust the selectors if Amazon changes their HTML structure
- Use this tool responsibly and consider Amazon's terms of service

## Output

The Excel file will contain columns for:
- Product Title
- Review Title
- Rating
- Review Body

## Disclaimer

This script is for educational purposes only. Web scraping may violate Amazon's terms of service. Use at your own risk.
