# Tasnim News Web Crawler

This repository contains a web crawler for the Tasnim News website, built using the Scrapy framework. The crawler collects news articles from various categories and exports the data into a CSV file.

## Features

- Crawls multiple categories from the Tasnim News website.
- Supports pagination to scrape multiple pages of news articles.
- Extracts key information from each news article, including the title, abstract, body, category, and publication time.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On windows
    ```bash
    venv\Scripts\activate
    ```
    - On Linux
    ```
    source venv/bin/activate
    ```
4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
## Usage    
To run the web crawler, execute the following command:
```
scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 tasnim.py -o tasnim_new/tasnim.csv
```
This command will start the crawling process and save the output to tasnim_new/tasnim.csv.

## Requirements
The project depends on the following Python packages, which are listed in requirements.txt:

```
rich==12.5.1
Scrapy==2.6.1
pyopenssl==22.0.0
cryptography==38.0.4
trafilatura==1.6.1
```
## Contributor

- **Haniye Mahmoodi**
  - Email: [haniye.mahmoodi01@gmail.com](mailto:haniye.mahmoodi01@gmail.com)

