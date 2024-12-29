# BBC News Web Scraper

A Python-based web scraper that extracts news articles from BBC News using Selenium and BeautifulSoup4. Built with the power of AI prompt engineering and ChatGPT.

## Features

- Extracts comprehensive article data including:
  - URLs
  - Headlines
  - Descriptions
  - Image URLs (highest resolution)
  - Image descriptions
  - Tags
  - Related URLs
- Handles dynamic JavaScript-rendered content
- Implements automatic scrolling for lazy-loaded content
- Manages missing data fields gracefully
- Outputs clean, structured JSON data

## Requirements

```text
Python 3.9+
Chrome WebDriver
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/bbc-news-scraper.git
cd bbc-news-scraper
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the main scraper:

```bash
python scrapper.py
```

2. The scraper will:

- Launch a headless Chrome browser
- Navigate to BBC News
- Scroll through the page to load all content
- Extract article data
- Save results to `output/news_scrapped.json`

## Output Format

```json
[
  {
    "url": "https://www.bbc.com/news/article-url",
    "image_url": "https://ichef.bbci.co.uk/news/image.jpg",
    "image_description": "Image description text",
    "headline": "Article headline",
    "description": "Article description",
    "tags": ["Tag1", "Tag2"]
  }
]
```

## Docker Support

Build and run the scraper in a container:

```bash
docker build -t bbc-news-scraper .
docker run bbc-news-scraper
```

## Project Structure

```
bbc-news-scraper/
├── scrapper.py         # Main scraper implementation
├── bad_scrapper.py     # Example of basic scraper (for comparison)
├── requirements.txt    # Project dependencies
├── Dockerfile          # Container configuration
├── output/             # Scraped data output directory
└── README.md           # Project documentation
```

## Technology Stack

- Python 3.9
- Selenium WebDriver
- BeautifulSoup4
- Chrome (headless mode)
- Docker

## Limitations

- Requires stable internet connection
- May need adjustments if BBC News changes their HTML structure
- Chrome WebDriver must be compatible with installed Chrome version

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with assistance from ChatGPT
- Inspired by the power of prompt engineering
- Thanks to the BBC News website structure documentation

## Author

Xavier Medina

## Contact

Email - xmedinavei@gmail.com
Project Link: [https://github.com/xmedinavei/python-web-scrapper](https://github.com/xmedinavei/python-web-scrapper)
