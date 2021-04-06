# Linkedin Job Scraper

Linkedin Jobs Scraper is a Python library for crawling jobs available on linkedin using specific keyword.

## Installation

Use git to clone this repository

```bash
git clone https://github.com/ghazimuharam/linkedin-job-scraper.git
```

## Prerequisite

This library use selenium with [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) to crawl the website, make sure you have selenium installed on your machine and make sure to set your chromedriver location by

```bash
export CHROMEDRIVER=~/chromedriver
```

Install the prerequisite library from requirements.txt

```bash
pip install -r requirements.txt
```

To use Google Bigquery as the storage, you need to Authenticate and Change TABLE_ID variable inside `./src/big_query.py`

```python
# Change this variable to your table_id of bigquery table
TABLE_ID = "yourproject.datasets.table"
```

To Authenticate with [Google Cloud API](https://cloud.google.com/docs/authentication/getting-started) you need to set your environment variable using command below

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
```

## Usage

Run the scraper with command below

```bash
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)