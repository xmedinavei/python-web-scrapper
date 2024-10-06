import os
import json
import requests
from bs4 import BeautifulSoup


def scrape_bbc_news():
    url = 'https://www.bbc.com/news'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = []

        # Finding headline elements in the HTML structure
        for item in soup.find_all(['h3', 'h2'], class_='gs-c-promo-heading__title'):
            headlines.append(item.get_text())

        # Save the scraped headlines in JSON format
        output_data = {"headlines": headlines}
        os.makedirs('output', exist_ok=True)
        with open('output/bad_scrapped.json', 'w') as json_file:
            json.dump(output_data, json_file, indent=4)
    else:
        print(f"Failed to fetch BBC News, Status code: {response.status_code}")


if __name__ == '__main__':
    scrape_bbc_news()
