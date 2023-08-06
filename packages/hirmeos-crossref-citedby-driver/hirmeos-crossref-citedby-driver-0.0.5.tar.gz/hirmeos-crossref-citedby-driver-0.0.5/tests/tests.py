from collections import namedtuple
import contextlib
import inspect
import io
import os
import unittest
from unittest.mock import patch

import bs4

from crossref_citedby_driver import (
    fetch_citation_xml,
    get_citation_data, 
    get_crossref_citations
)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class CrossRefDriverTest(unittest.TestCase):
    """Run unit tests for the crossref cited-by driver module."""
    def setUp(self):
        self.my_data_path = os.path.join(
            THIS_DIR, 'CrossrefCitations_2023-05-25.xml'
        )
        with open(self.my_data_path, 'r') as f:
            self.raw_data = f.read()

        self.maxDiff = None

    @patch("crossref_citedby_driver.request_citation", autospec=True)
    def test_fetch_citation_xml_successful_response(
        self, 
        mock_call_external_api: unittest.mock
    ) -> None:
        """Test we get a successful response from fetch_citation_xml."""
        mock_call_external_api.return_value.status_code = 200
        mock_call_external_api.return_value.text ='There was a successful response'
        response_text, status_code = fetch_citation_xml(
            username='username_test', 
            password='pass_test', 
            doi_prefix='12.3456789',
            start_date='2023-02-01',
            end_date='2023-02-02',
        )
        self.assertEqual(
            status_code,
            200
        )        
        self.assertEqual(
            response_text,
           'There was a successful response'
        )

    @patch("crossref_citedby_driver.request_citation", autospec=True)
    def test_fetch_citation_xml_unsuccessful_response(
        self, 
        mock_call_external_api: unittest.mock
    ) -> None:
        """The sys.stderr.write() gets fired because the response is not 200."""
        mock_call_external_api.return_value.text ='There was a unsuccessful response'
        f = io.StringIO()
        with contextlib.redirect_stderr(f):
            fetch_citation_xml(
                username='username_test', 
                password='pass_test', 
                doi_prefix='12.3456789',
                start_date='2023-02-01',
                end_date='2023-02-02',
            )
        sys_output ="""
        Could not retrieve cited-by citations 
        (<MagicMock name='request_citation().reason' id='140112213126896'>) 
        - Request parameters: {'usr': 'username_test', 'pwd': 'pass_test', 
        'doi': '<doi type="journal_article">12.3456789/test.2023</doi>', 
        'startDate': '2023-02-01', 'endDate': '2023-02-02'}); url: 
        https://doi.crossref.org/servlet/getForwardLinks
        """
        self.assertEqual(
            inspect.cleandoc(sys_output)[1:30],
            str(f.getvalue())[1:30]
        )

    def test_get_crossref_citations(self) -> None:
        """Test the result is correctly extracted from the xml."""
        xml_test ="""
            <journal_cite fl_count="0">
            <issn type="print">3456789</issn>
            <journal_title>Journal Test</journal_title>
            <journal_abbreviation>Journal Test</journal_abbreviation>
            <article_title>Quality assurance and safety Test</article_title>
            <contributors>
            <contributor contributor_role="author" first-author="true" sequence="first">
            <given_name>Test Name</given_name>
            <surname>Test Surname</surname>
            </contributor>
            <contributor contributor_role="author" first-author="false" sequence="additional">
            <given_name>Test Name 2</given_name>
            <surname>Test Surname 2</surname>
            </contributor>
            <year>2023</year>
            <publication_type>full_text</publication_type>
            <doi type="journal_article">12.3456789/test.12345</doi>
            </contributors>
            </journal_cite>
       """

        citations = get_crossref_citations(
            self.raw_data,'12.3456789/2012.12.006'
        )
        self.assertEqual(
            str(next(iter(citations.values()))[0]),            
            inspect.cleandoc(xml_test)   
        )
    
    def test_get_citation_data_and_determine_timestamp(self) -> None:
        """The get citation data method returns the expected values."""
        Citation = namedtuple('Citation', ['cited_by', 'timestamp'])
        citation_entry = bs4.BeautifulSoup(
            (
                '<journal_cite>'
                '   <doi type="journal_article">12.3456789/test.2023</doi>'
                '   <year>2022</year>'
                '</journal_cite>'
            ),
            features="xml"
        )
        citation_date = '2023-01-01'
        returned = get_citation_data(
            citation_entry,
            citation_date
        )
        self.assertEqual(
            returned,
            Citation(cited_by='12.3456789/test.2023', timestamp='2022-01-01 00:00:00')
        )
