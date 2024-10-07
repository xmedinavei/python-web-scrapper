from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json
import os
import re
import time


def extract_highest_res_image(srcset):
    # Split the srcset into individual image entries
    image_entries = srcset.split(',')
    max_width = 0
    max_res_image_url = ''
    for entry in image_entries:
        parts = entry.strip().split(' ')
        if len(parts) >= 2:
            url = parts[0]
            width = parts[1]
            width_value = int(re.findall(r'\d+', width)[0])
            if width_value > max_width:
                max_width = width_value
                max_res_image_url = url
    return max_res_image_url


def scroll_down(driver):
    """Function to scroll down the page to trigger lazy loading of content."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # Break the loop if no more content is loaded
            break
        last_height = new_height


def main():
    url = 'https://www.bbc.com/news'

    # Set up Selenium with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the page
    driver.get(url)
    time.sleep(5)  # Wait for the initial content to load

    # Scroll down the page to load all content
    scroll_down(driver)

    # Get the page source after JavaScript has rendered
    html_content = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')

    articles_data = []

    # Find the main content
    main_content = soup.find('main', id='main-content')
    if not main_content:
        print("Main content not found")
        return

    # Find all sections within the main content
    sections = main_content.find_all('section')

    for section in sections:
        article_cards = section.find_all(['div', 'article'], attrs={
                                         'data-testid': re.compile('.*-card|.*-article|.*-content')})

        for article_card in article_cards:
            article_data = {}

            # Extract the article link
            anchor = article_card.find(
                'a', attrs={'data-testid': 'internal-link'}, href=True)
            if anchor:
                article_url = anchor.get('href', '')
                if article_url.startswith('/'):
                    article_url = 'https://www.bbc.com' + article_url
                article_data['url'] = article_url

                # Extract the image
                img_tag = anchor.find('img')
                if img_tag:
                    srcset = img_tag.get('srcset', '')
                    if srcset:
                        image_url = extract_highest_res_image(srcset)
                    else:
                        image_url = img_tag.get('src', '')
                    if 'grey-placeholder' not in image_url:
                        article_data['image_url'] = image_url
                        article_data['image_description'] = img_tag.get(
                            'alt', '')
                    else:
                        article_data['image_url'] = ''
                        article_data['image_description'] = ''
                else:
                    article_data['image_url'] = ''
                    article_data['image_description'] = ''
            else:
                article_data['url'] = ''
                article_data['image_url'] = ''
                article_data['image_description'] = ''

            # Extract the headline and description
            headline = article_card.find(['h1', 'h2', 'h3'], attrs={
                                         'data-testid': 'card-headline'})
            article_data['headline'] = headline.get_text(
                strip=True) if headline else ''
            description = article_card.find(
                'p', attrs={'data-testid': 'card-description'})
            article_data['description'] = description.get_text(
                strip=True) if description else ''

            # Extract tags
            tags = article_card.find_all(
                'span', attrs={'data-testid': 'card-metadata-tag'})
            article_data['tags'] = [tag.get_text(strip=True) for tag in tags]

            # Add to article data list
            if article_data['url'] or article_data['headline']:
                articles_data.append(article_data)

    # Ensure output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write data to JSON file
    output_file = os.path.join(output_dir, 'news_scrapped.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(articles_data, f, ensure_ascii=False, indent=4)

    print(f"Scraped {len(articles_data)} articles and saved to {output_file}")


if __name__ == '__main__':
    main()
