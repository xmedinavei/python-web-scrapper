# 📰 BBC News Web Scraper 🌐

![GitHub repo size](https://img.shields.io/github/repo-size/xmedinavei/python-web-scrapper) ![GitHub issues](https://img.shields.io/github/issues/xmedinavei/python-web-scrapper) ![GitHub forks](https://img.shields.io/github/forks/xmedinavei/python-web-scrapper?style=social) ![GitHub stars](https://img.shields.io/github/stars/xmedinavei/python-web-scrapper?style=social)   
![Python](https://img.shields.io/badge/Python-3.9-blue) ![Docker](https://img.shields.io/badge/Docker-Enabled-blue) ![OpenAI-ChatGPT](https://img.shields.io/badge/OpenAI-ChatGPT-green)

A **Python-based web scraper** that extracts news articles from BBC News using **Selenium** and **BeautifulSoup4**.  
Built with the power of **AI Prompt Engineering** and **ChatGPT**.

---

## ✨ Features

- 📜 Extracts comprehensive article data, including:
  - 🔗 URLs
  - 📰 Headlines
  - 🖼️ Image URLs (highest resolution)
  - ✏️ Image descriptions
  - 🌂 Tags
  - 🔄 Related URLs
- ⚡ Handles dynamic JavaScript-rendered content
- 💡 Implements automatic scrolling for lazy-loaded content
- ❌ Manages missing data fields gracefully
- 📂 Outputs clean, structured JSON data

---

## 📋 Requirements

- **Python 3.9+**  
- **Chrome WebDriver**

---

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/xmedinavei/python-web-scrapper.git
   cd python-web-scrapper
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

1. **Run the scraper**:

   ```bash
   python scrapper.py
   ```

   🎯 The scraper will:
   - Launch a headless Chrome browser
   - Navigate to BBC News
   - Scroll through the page to load all content
   - Extract article data
   - Save results to `output/news_scrapped.json`

---

## 🖂️ Output Format

Here's an example of the output JSON structure:

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

---

## 🐳 Docker Support

**Build and run** the scraper in a container:

```bash
docker build -t bbc-news-scraper .
docker run bbc-news-scraper
```

---

## 🏠 Project Structure

```plaintext
bbc-news-scraper/
├── scrapper.py         # Main scraper implementation
├── bad_scrapper.py     # Example of basic scraper (for comparison)
├── requirements.txt    # Project dependencies
├── Dockerfile          # Container configuration
├── output/             # Scraped data output directory
└── README.md           # Project documentation
```

---

## 🔧 Technology Stack

- **Python 3.9**  
- **Selenium WebDriver**  
- **BeautifulSoup4**  
- **Chrome (headless mode)**  
- **Docker**

---

## ⚠️ Limitations

- Requires a stable internet connection  
- May need adjustments if BBC News changes their HTML structure  
- Chrome WebDriver must be compatible with the installed Chrome version  

---

## 🤝 Contributing

Contributions are welcome! 🚀  
Please follow these steps:

1. **Fork the repository**  
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)  
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)  
4. **Push to the branch** (`git push origin feature/AmazingFeature`)  
5. **Open a Pull Request**

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 💡 Further Reading

Explore these resources to deepen your understanding of **prompt engineering** and **LLMs (Large Language Models)**:

- [A Beginner's Guide to Prompt Engineering](https://www.prompting.ai/guide) - Learn the basics of crafting effective prompts for AI systems.
- [Applications of Large Language Models](https://huggingface.co/transformers/) - Dive into practical applications of LLMs like GPT.
- [OpenAI's Documentation](https://platform.openai.com/docs/) - Get insights into using OpenAI APIs effectively.
- [How to Create a Web Scraper Without Writing Code](https://xaviermedina.hashnode.dev/how-to-create-a-web-scraper-without-writing-code-unlocking-the-power-of-prompt-engineering-with-chatgpt) - Learn the detailed process of building this project.

## 💡 Acknowledgments

- Built with assistance from **ChatGPT** 🤖  
- Inspired by the power of **prompt engineering** 🔋 ([Learn more about prompt engineering](https://xaviermedina.hashnode.dev/how-to-create-a-web-scraper-without-writing-code-unlocking-the-power-of-prompt-engineering-with-chatgpt#prompt-engineering))
- Thanks to the **BBC News** website structure documentation 🙌

---

## 👤 Author

**Xavier Medina**  

- 📧 Email: [xmedinavei@gmail.com](mailto:xmedinavei@gmail.com)  
- 🔗 Blog Post: [How to Create a Web Scraper Without Writing Code](https://xaviermedina.hashnode.dev/how-to-create-a-web-scraper-without-writing-code-unlocking-the-power-of-prompt-engineering-with-chatgpt)

### 📃 Blog Insights
The blog post takes a deep dive into the **prompt engineering techniques** used to design this scraper. Learn how **AI-driven development** simplifies coding challenges and enhances developer productivity! Explore the [full blog here](https://xaviermedina.hashnode.dev/how-to-create-a-web-scraper-without-writing-code-unlocking-the-power-of-prompt-engineering-with-chatgpt).
