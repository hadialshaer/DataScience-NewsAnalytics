# 🌐 AlMayadeen News Scraper

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and efficient Web Scraper that extracts, analyzes, and visualizes data from the AlMayadeen news website. Utilizing advanced data analysis techniques such as sentiment analysis and entity recognition, this application dives deep into textual data to extract meaningful insights.
<div align="center">
  <a href="https://github.com/hadialshaerr"><strong>View Profile</strong></a>
    <br />
    <br />
    <a href="https://github.com/hadialshaerr/DgPad2024-DataScience-WebScraping/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
    ·
    <a href="https://github.com/hadialshaerr/DgPad2024-DataScience-WebScraping/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </p>
</div>

![Quick Demo of Data Visualization](Task_2_3/static/images/Visualizations.gif)

## 📋 Table of Contents

- [Detailed walkthrough videos of the AlMayadeen News Scraper](#detailed-walkthrough-videos-of-the-almayadeen-news-scraper)
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Installation Guide](#-installation-guide)
- [Usage](#-usage)
- [Customization](#customization)
- [Project Structure](#-project-structure)
- [Results](#-results)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

## Detailed walkthrough videos of the AlMayadeen News Scraper

  - Task_1: Extract articles, gather relevant metadata, and save this information into JSON files organized by month.

[![Presentation Video](https://img.youtube.com/vi/HgRxg2Gz0MY/maxresdefault.jpg)](https://youtu.be/HgRxg2Gz0MY)

  - Task_2: Store Data in MongoDB, and build a simple web service using Flask that allows access and analyze the data through 30 easy-to-use API endpoints.

[![Presentation Video](https://img.youtube.com/vi/VscFSu7S72A/maxresdefault.jpg)](https://youtu.be/VscFSu7S72A)

  - Task_3: Visualize the data using amCharts to create interactive and visually appealing charts that help you more effectively understand the patterns and insights in the data.

[![Presentation Video](https://img.youtube.com/vi/_ZR1FFW3nMU/maxresdefault.jpg)](https://youtu.be/_ZR1FFW3nMU)

## 🔍 Overview

The AlMayadeen News Scraper is a full-featured data analysis application that extracts valuable information from articles and visualizes it.
It uses advanced data analysis techniques like sentiment analysis and entity recognition. 
This project aims to facilitate data analysis and research on news content from the Middle East.
It extracts deeper insights from textual data and presents these insights meaningfully.

## 🚀 Key Features

- **Intelligent Sitemap Parsing**: Efficiently extracts article URLs from monthly sitemaps
- **Comprehensive Article Scraping**: Captures metadata, full text, and associated media information
- **Structured Data Storage**: Organizes scraped data into year-month based JSON files
- **Robust Error Handling**: Ensures smooth operation even when encountering network issues or unexpected page structures
- **Configurable Limits**: Allows easy adjustment of scraping boundaries to suit different needs

## 🔧 Installation Guide

1. Clone the repository:
   ```
   git clone https://github.com/hadialshaerr/DgPad-DataScience-WebScraping.git
   cd DgPad-DataScience-WebScraping
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies using:
   ```
   pip install -r requirements.txt
   ```
   or using pip:
   ```
   pip install requests beautifulsoup4 lxml
   ```

## 🚀 Usage

1. **Run the main script to start the scraping process:**

   ```
   python web_scraper_main.py
   ```

   This will start the process of parsing the sitemap, scraping articles, and saving the data into JSON files.

2. **Output:**

   The scraped data will be stored in the `data_articles/` directory, with each file named according to the year and month (e.g., `articles_2024_08.json`).

2. **Dashboard with visualized endpoints**

   Run the `app.py` script, and open the url that refers to your local server.

2. **Enjoy the show 😉**
   
## Customization

- **Storage Path:** Update the directory path in `FileUtilityClass.py` to change where JSON files are stored.
- **Target Classes:** Modify `ArticleScraperClass.py` to customize which `<p>` tags or classes to scrape.

## 📁 Project Structure

```
DgPad2024-DataScience-WebScraping/
│
├── data_articles             # Folder that contains JSON files
├── Article.py                # Article data structure definition
├── ArticleScraperClass.py    # Article scraping logic
├── FileUtilityClass.py       # Data saving utilities
├── requirements.txt          # Project dependencies
├── SiteParserClass.py        # Sitemap parsing functionality
├── web_scraper_main.py       # Main execution script
└── README.md                 # Project documentation
```

## 📊 Results

Our scraper has successfully extracted a wealth of information from the AlMayadeen website. Here are some visual representations of our results:

*Execution process in the terminal*
![Execution Process](Task_1/Verified_Results_Screenshots/1.png)

*Total number of articles scraped*
![Scraping Completion](Task_1/Verified_Results_Screenshots/2.png)

*JSON files generated from the scraped data*
![Data Output](Task_1/Verified_Results_Screenshots/3.png)

*For a visual representation, refer to the GIF.*
## 🛣 Roadmap

- [ ] Implement multi-threading for faster scraping
- [ ] Add support for older archive pages
- [ ] Develop a user interface for easy configuration
- [ ] Integrate with a database for more efficient storage
- [ ] Implement advanced text analysis features
- [ ] ... ... more coming soon

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Hadi Al-Shaer**

- GitHub: [@hadialshaerr](https://github.com/hadialshaerr)
- reach me: hadialshaerrr@gmail.com

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⚠️ **Disclaimer**: This scraper is intended for educational and research purposes only. Always respect the website's robots.txt file and terms of service when scraping content.
