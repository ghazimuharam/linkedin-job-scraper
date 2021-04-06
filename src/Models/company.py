from selenium.common.exceptions import NoSuchElementException


class Company:
    """
    A class used to store Company information
    from Crawling

    Attributes
    ----------
    name : str
        Name of the company
    industry : bigquery.Client
        Industry of the company
    company_size : str
        Size of the company
    headquarters : bigquery.Client
        Headquarters location of the company

    """

    name = None
    industry = None
    company_size = None
    headquarters = None

    def __init__(self, url, driver) -> None:
        """
        Parameters
        ----------
        url : str
            Url to navigate with selenium
        driver : webdriver
            Selenium webdriver object

        Returns
        -------
        None
        """
        self.url = url
        self.driver = driver
        self.set_company_data()

    def get_company_profile(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        dict
            a dictionary of all company information
        """
        return {'company_name': self.name, 'industry': self.industry,
                'company_size': self.company_size, 'headquarters': self.headquarters}

    def set_company_data(self):
        """Set instances variable from crawling the company data

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.driver.get(self.url)
        self.set_company_name()
        self.set_company_size()
        informations = self.get_company_informations()
        self.set_company_industry(informations)
        self.set_company_headquarters(informations)

    def get_company_informations(self):
        return self.driver.find_elements_by_xpath(
            '//dd[@class="org-page-details__definition-text t-14 t-black--light t-normal"]')

    def set_company_name(self):
        try:
            self.name = self.driver.find_element_by_xpath(
                '//span[@dir="ltr"]').text.strip()
        except NoSuchElementException:
            print("Company name not found")

    def set_company_size(self):
        try:
            self.company_size = self.driver.find_element_by_xpath(
                '//dd[@class="org-about-company-module__company-size-definition-text t-14 t-black--light mb1 fl"]'
            ).text
        except NoSuchElementException:
            print("Company size not found")

    def set_company_industry(self, informations):
        try:
            self.industry = informations[1].text
        except IndexError:
            print("Company industry not found")

    def set_company_headquarters(self, informations):
        try:
            self.headquarters = informations[2].text
        except IndexError:
            print("Company headquarters not found")
