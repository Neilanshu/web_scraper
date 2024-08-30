import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to clean unwanted symbols from text
def clean_text(text):
    text = re.sub(r'\|[^\|]*\r?\n', '', text)  # Remove notations like |0⟩
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

# Function to extract and format URLs from content
def extract_urls(content):
    urls = re.findall(r'http[s]?://\S+', content)
    return urls

# Function to scrape the entire webpage
def scrape_entire_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page title
    title = soup.find('h1', id='firstHeading').text.strip()

    # Extract headings, paragraphs, and images
    headings = soup.find_all(['h2', 'h3', 'h4'])
    paragraphs = soup.find_all(['p', 'li'])
    images = soup.find_all('img')

    data = []

    # Initialize current section and subsection
    current_section = ""
    current_subsection = ""

    # Process headings
    for heading in headings:
        heading_text = clean_text(heading.text)
        if heading.name == 'h2':
            current_section = heading_text
            current_subsection = ""
            data.append([current_section, '', '', '', '', ''])  # Section row
        elif heading.name in ['h3', 'h4']:
            current_subsection = heading_text
            data.append([current_section, current_subsection, '', '', '', ''])  # Subsection row

    # Process paragraphs and list items
    for paragraph in paragraphs:
        text = clean_text(paragraph.text)
        urls = extract_urls(text)
        data.append([current_section, current_subsection, text, ', '.join(urls), '', ''])

    # Process images
    for img in images:
        img_src = img.get('src')
        img_alt = clean_text(img.get('alt', ''))
        if img_src:
            img_url = requests.compat.urljoin(url, img_src)
            data.append(['', '', '', '', img_alt, img_url])

    return title, data

# Function to save the scraped content to a CSV file
def save_to_csv_file(title, data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Section', 'Subsection', 'Content', 'URLs', 'Image Title', 'Image URL'])
        writer.writerow(['Title', '', '', '', '', title])
        writer.writerows(data)

# Main execution block
if __name__ == "__main__":
    url = "https://en.m.wikipedia.org/wiki/Quantum_computing"
    title, data = scrape_entire_webpage(url)
    save_to_csv_file(title, data, "organized_quantum_computing_wikipedia.csv")
    print("Webpage content scraped and saved to organized_quantum_computing_wikipedia.csv")