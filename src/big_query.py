from google.cloud import bigquery


class GoogleBigQuery:
    """
    A class used to represent GoogleBigQuery Object

    Attributes
    ----------
    TABLE_ID : str
        table identifier on Google BigQuery
    client : bigquery.Client
        Object of Google Big Query Client

    """

    # Change this variable to your table_id of bigquery table
    TABLE_ID = "yourproject.datasets.table"
    client = bigquery.Client()

    def insert_data(self, crawl_data, keyword):
        """Insert data into Google BigQuery
        Parameters
        ----------
        crawl_data : dict
            Dictionary of Job object
        keyword : str
            Keyword used to get Job object

        Returns
        -------
        None
        """

        query = [self.query_builder(crawl_data, keyword)]

        # Make an API request.
        errors = self.client.insert_rows_json(self.TABLE_ID, query)
        if errors == []:
            print(f"Added Job_id {crawl_data['job_id']}.")
        else:
            print("Encountered errors while inserting rows({}): {}".format(
                errors, crawl_data['job_id']))

    def query_builder(self, crawl_data, keyword):
        """JSON Query builder from Data
        Parameters
        ----------
        crawl_data : dict
            Dictionary of Job object
        keyword : str
            Keyword used to get Job object
        Job_id : int
            Unique identifier of Job Object

        Returns
        -------
        Dict
            Dictionary of JSON Query
        """

        return {u"Number_of_applicants": crawl_data['number_of_applicants'],
                u"posting_time": crawl_data['posting_time'], u"seniority_level":
                crawl_data['seniority_level'], u"employment_type": crawl_data['employment_type'],
                u"job_function": crawl_data['job_function'], u"company_name":
                crawl_data['company_name'], u"company_size": crawl_data['company_size'],
                u"industry": crawl_data['industry'], u"description": crawl_data['description'],
                u"keyword": keyword, u"Job_id": crawl_data['job_id']}
