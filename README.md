# Web Scraper

## Overview

The `web_scraper` project is a Python-based tool designed to scrape data from a specified Wikipedia page and organize it into a CSV file. The scraper extracts headers, subheaders, content, URLs, and image titles/URLs, optimizing data for better usability and structure.

## Features

- **Scraping**: Extracts structured data from a Wikipedia page.
- **Data Organization**: Organizes data into specific columns:
  - **Section**: Main section headings.
  - **Subsection**: Subheadings within each section.
  - **Content**: Textual content.
  - **URLs**: URLs found within the content.
  - **Image Title**: Titles or alt text of images.
  - **Image URL**: URLs of images.
- **Excludes Unwanted Data**: Filters out irrelevant symbols and notations.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/USERNAME/web_scraper.git
   cd web_scraper
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Install the required Python packages using `pip`:

   ```bash
   pip install requests beautifulsoup4
   ```

   Optionally, create a `requirements.txt` file:

   ```plaintext
   requests
   beautifulsoup4
   ```

   Install dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Scraper**

   Execute the Python script to start the scraping process:

   ```bash
   python wikipedia_scraper.py
   ```

   This will scrape the specified Wikipedia page and save the organized content into `organized_quantum_computing_wikipedia.csv`.

2. **Script Details**

   - **URL**: The URL of the Wikipedia page to be scraped is defined in the script.
   - **Data Columns**:
     - **Section**: Main sections of the Wikipedia page.
     - **Subsection**: Subheadings under each section.
     - **Content**: Text content.
     - **URLs**: Extracted URLs.
     - **Image Title**: Titles or alt text of images.
     - **Image URL**: URLs of images.

## Code Explanation

1. **Import Libraries**

   ```python
   import requests
   from bs4 import BeautifulSoup
   import csv
   import re
   ```

2. **Functions**

   - **`clean_text(text)`**: Removes unwanted symbols and extra spaces from text.
   - **`extract_urls(content)`**: Extracts URLs from a given text.
   - **`scrape_entire_webpage(url)`**: Scrapes the content from the specified URL, organizes it into sections, subsections, and extracts images and URLs.
   - **`save_to_csv_file(title, data, filename)`**: Saves the scraped data into a CSV file with defined columns.

3. **Main Execution Block**

   The script initializes the URL, calls the scraping function, and saves the data to a CSV file.

## Sample Output

The output file `organized_quantum_computing_wikipedia.csv` will have columns:

- **Section**: Main sections of the Wikipedia page.
- **Subsection**: Subheadings under each section.
- **Content**: Text content.
- **URLs**: Extracted URLs.
- **Image Title**: Titles or alt text of images.
- **Image URL**: URLs of images.

## Troubleshooting

- **ModuleNotFoundError**: Ensure you have installed the required libraries using `pip`.
- **Scraping Errors**: Check if the URL is correct and accessible. Review the HTML structure of the page to ensure the scraper’s selectors are accurate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature-branch`).
5. Create a Pull Request on GitHub.
