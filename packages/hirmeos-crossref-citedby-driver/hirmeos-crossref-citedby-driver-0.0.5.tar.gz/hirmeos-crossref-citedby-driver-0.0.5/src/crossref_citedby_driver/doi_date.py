from dataclasses import dataclass
from logging import getLogger

from bs4 import BeautifulSoup
import requests
from requests.models import Response


logger = getLogger(__name__)


@dataclass
class CrossrefDOIDateChecker:

    tech_email: str

    def get_prime_doi(self, aliased_doi: str) -> str:
        """For aliased DOIs, determine the new DOI.

        Args:
            aliased_doi (str): Aliased DOI value

        Returns:
            str: Resolved DOI value that the aliased DOI points to.
        """
        response = requests.get(
            'https://doi.crossref.org/servlet/query',
            params=dict(
                pid=self.tech_email,
                format='unixsd',
                id=aliased_doi
            )
        )

        xml_content = response.content
        xml_data = BeautifulSoup(xml_content, features="xml")

        items = xml_data.find_all('crm-item')
        for item in items:
            if item.attrs.get('name') == 'prime-doi':
                return item.text

        return ''

    def query_doi_crossref(self, doi: str) -> Response:
        """Make a request to crossref works endpoint to get info about a DOI.

        Args:
            doi (str): DOI of the work.

        Returns:
            Response: Unprocessed response received from the API.
        """
        return requests.get(
            f'https://api.crossref.org/v1/works/{doi}',
            params=dict(mailto=self.tech_email)
        )

    def get_date_value(self, doi):
        response = self.query_doi_crossref(doi)

        if response.status_code == 404:
            prime_doi = self.get_prime_doi(doi)
            if not prime_doi:
                raise ValueError('Invalid DOI')

            response = self.query_doi_crossref(prime_doi)
            if response.status_code == 404:
                raise ValueError('Prime DOI not found')

        try:
            response_message = response.json()['message']
        except ValueError as e:
            logger.info(f'Error {e}')
            raise

        return self.fetch_publish_date(response_message)

    # This is hardly exhaustive - but better than previous implementations.
    @staticmethod
    def fetch_publish_date(message: dict) -> str:
        """Get best guess for date published, based on the crossref response.

        Args:
            message: Message portion of the response from crossref.

        Returns:
            str: Publication date in "YYYY-MM-DD" format.
        """
        keys = ['published', 'published-print', 'published-online', 'created']
        for key in keys:
            if key in message and len(message[key]['date-parts'][0]) == 3:
                year, month, day = message[key]['date-parts'][0]
                month, day = str(month).zfill(2), str(day).zfill(2)
                return f'{year}-{month}-{day}'

        raise ValueError('No valid publish date found')
