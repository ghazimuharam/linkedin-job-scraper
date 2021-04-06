from fake_useragent import UserAgent
import re

from selenium.webdriver.support.wait import WebDriverWait


class Crawl():
    """
    Crawl class to Bridge the functionality
    of selenium

    Attributes
    ----------
    BASE_API_JOBS : str
        BASE URL of Jobs index
    USER_AGENT : list
        list of UserAgent for UA rotating
    driver : webdriver
        Selenium webdriver object

    """

    BASE_API_JOBS = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={}&location=Indonesia&start={}"
    USER_AGENT = UserAgent()

    def __init__(self, driver) -> None:
        """
        Parameters
        ----------
        driver : webdriver
            Selenium webdriver object
        """

        self.driver = driver
        self.driver.get(
            "https://www.linkedin.com/?allowUnsupportedBrowser=true")

    def get_page(self, url):
        """Navigate using selenium and rotating UserAgent

        Parameters
        ----------
        url : str
            URL to get with selenium
        """

        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": self.USER_AGENT.random})
        self.driver.get(url)

    def get_all_job_ids(self, keywords) -> list:
        """Gets all job ids from BASE_API_JOBS

        Parameters
        ----------
        keywords : str
            Job search keyword

        Returns
        -------
        list
            a list of all job ids found
        """
        stop_loop = False
        page_num = 0

        job_ids = []
        while (stop_loop != True):
            self.get_page(self.BASE_API_JOBS.format(keywords, str(page_num)))
            jobs = self.driver.find_elements_by_tag_name('li')
            if not jobs:
                break

            for job in jobs:
                link = job.find_element_by_class_name(
                    'result-card__full-card-link'
                ).get_attribute('href')
                id_matching = re.search("-(\d*)\?", link)
                job_ids.append(id_matching.group(1))

            page_num += 25
        return job_ids
