from selenium.common.exceptions import NoSuchElementException
from .company import Company


class Job:
    """
    A class used to represent Job Object

    Attributes
    ----------
    BASE_DATA_JOB : str
        BASE URL of Jobs data
    number_applicants : str
        Number of current applicants of Job
    posting_time : str
        posting_time of Job
    seniority_level : str
        seniority_level of Job data
    employement_type : str
        employement_type of Job
    job_function : str
        job_function of Job
    description : str
        description of Job
    job_id : int
        Unique id of Job

    """

    BASE_DATA_JOB = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}"

    number_applicants = None
    posting_time = None
    seniority_level = None
    employement_type = None
    job_function = None
    description = None

    def __init__(self, job_id, driver) -> None:
        """
        Parameters
        ----------
        job_id : int
            Unique id of job object
        driver : webdriver
            Selenium webdriver object
        """
        self.job_id = job_id
        self.driver = driver
        self.set_job_data()

    def get_job_data(self):
        """Set instances variable from crawling the company data

        Parameters
        ----------
        None

        Returns
        -------
        Dict
            Dictionary of job object
        """
        crawl_data = {}
        crawl_data['number_of_applicants'] = self.number_applicants
        crawl_data['posting_time'] = self.posting_time
        crawl_data['seniority_level'] = self.seniority_level
        crawl_data['employment_type'] = self.employement_type
        crawl_data['job_function'] = self.job_function
        crawl_data['description'] = self.description
        crawl_data['job_id'] = self.job_id

        company = self.driver.find_element_by_xpath(
            '//h3[@class="topcard__flavor-row"]/span[@class="topcard__flavor"]'
        )

        try:
            url = company.find_element_by_tag_name(
                "a").get_attribute('href').replace("?trk=public_jobs_topcard_org_name", "/about/")
            crawl_data.update(
                Company(url=url, driver=self.driver)
                .get_company_profile()
            )
        except NoSuchElementException:
            crawl_data['company_name'] = company.text
            crawl_data['company_size'] = "Not listed"
            crawl_data['industry'] = "Not listed"

        return crawl_data

    def get_job_page(self):
        """Navigate using selenium to BASE_DATA_JOB

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.driver.get(self.BASE_DATA_JOB.format(self.job_id))

    def set_job_data(self):
        """Set instances variable from crawling the job data

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.get_job_page()
        self.set_applicants_number()
        self.set_posting_time()
        self.set_seniority_level()
        self.set_employement_type()
        self.set_job_function()
        self.set_description()

    def set_applicants_number(self):
        number_applicants = self.driver.find_element_by_class_name(
            "num-applicants__caption"
        ).text
        number_applicants = 0 if "Be among the first" in number_applicants else number_applicants

        self.number_applicants = number_applicants

    def set_posting_time(self):
        self.posting_time = self.driver.find_element_by_class_name(
            "posted-time-ago__text"
        ).text

    def set_seniority_level(self):
        self.seniority_level = self.driver.find_element_by_xpath(
            '//li[@class="job-criteria__item"][1]/span[@class="job-criteria__text job-criteria__text--criteria"][1]'
        ).text

    def set_employement_type(self):
        self.employement_type = self.driver.find_element_by_xpath(
            '//li[@class="job-criteria__item"][2]/span[@class="job-criteria__text job-criteria__text--criteria"][1]'
        ).text

    def set_job_function(self):
        functions = self.driver.find_elements_by_xpath(
            '//li[@class="job-criteria__item"][3]/span[@class="job-criteria__text job-criteria__text--criteria"]'
        )
        job_function = ""
        for function in functions:
            job_function += function.text + " "

        self.job_function = job_function

    def set_description(self):
        self.description = self.driver.find_element_by_xpath(
            '//section[@class="show-more-less-html"]'
        ).text
