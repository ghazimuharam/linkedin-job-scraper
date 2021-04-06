#!/usr/bin/env python3
from time import sleep
from src.Models.job import Job
from src import Crawl, actions, GoogleBigQuery
from selenium import webdriver

"""Linkedin Jobs Scraper
Linkedin Jobs Scraper is a Python library for crawling jobs available on linkedin using specific keyword.
"""

__author__ = "Muhammad Ghazi Muharam"
__version__ = "0.1.0"
__license__ = "MIT"


KEYWORDS = ["Data Engineer", "Data Scientist",
            "Data Analyst", "Business Intelligence Analyst"]
EMAIL = "yourlinkedinemail"
PASSWORD = "yourlinkedinpassword"


def main():
    """
    Main method of Linkedin-job-scraper
    """
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Authenticate with linkedin account
    actions.login(driver, EMAIL, PASSWORD)

    # Initialize Crawler
    crawler = Crawl(driver)

    # Initialize GoogleBigQuery Client API
    Gbq = GoogleBigQuery()

    for keyword in KEYWORDS:
        print(f"Crawling {keyword} available job")
        # Get job_ids
        job_ids = crawler.get_all_job_ids(keyword)

        print(f"Found {len(job_ids)} jobs of {keyword}")
        for job_id in job_ids:
            # Create Job Object
            job = Job(job_id=job_id, driver=driver)

            # Don't hit the API too often
            sleep(1)

            # Get all Job Data
            job_data = job.get_job_data()

            # Insert to Google Big Query
            Gbq.insert_data(job_data, keyword)

        # Don't hit the API too often
        sleep(5)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
