"""
"""

import datetime
import re

import bs4
import pandas as pd
import requests


class CIKLookup:
    """
    API wrapper for the SEC `CIK Lookup`_ tool.

    .. py:attribute:: address

        The URL address of the CIK Lookup tool.

        :type: str
        :value: https://www.sec.gov/cgi-bin/cik_lookup

    :param name: The company name (i.e., the search term)

    .. CIK Lookup: https://www.sec.gov/cgi-bin/cik_lookup
    """
    address = "https://www.sec.gov/cgi-bin/cik_lookup"

    def __init__(self, name: str):
        self.name = name

        with requests.post(
            self.address, data={"company": self.name}, timeout=100
        ) as response:
            self._soup = bs4.BeautifulSoup(response.text, features="lxml")

    @property
    def count(self) -> int:
        """
        The number of CIK Lookup search results.
        """
        element = self._soup.select_one("table tr > td:last-child > p")

        return int(re.search(r"\d+", element.text).group())

    @property
    def truncated(self) -> bool:
        """
        Whether the CIK Lookup search results were truncated.

            The search will return as many as 100 records that match your keyword(s), but after
            that it will truncate (cut off) the list. If this happens, it means that you need to be
            more specific.
        """
        element = self._soup.select_one("table tr > td:last-child > p")

        return "truncated" in element.text

    @property
    def results(self) -> pd.DataFrame:
        """
        The CIK Lookup search results.
        """
        if self.count == 0:
            return pd.DataFrame({})
        element = self._soup.select_one("table tr > td:last-child > pre:last-of-type")

        data = [[y.strip() for y in x.split(maxsplit=1)] for x in element.text.split("\n") if x]
        cik_code, company_name = zip(*data)
        href = [f"https://sec.gov/{e.attrs['href']}" for e in element.select("a")]

        return pd.DataFrame(
            {"CIK Company": cik_code, "Company Name": company_name, "URL": href}
        )

    @property
    def timestamp(self) -> datetime.datetime:
        """
        The timestamp of the CIK Lookup search query.
        """
        element = self._soup.select_one("table > tr > td:last-child > p:last-of-type")

        return datetime.datetime.strptime(
            element.text.strip(), "Generated at %H:%M:%S EDT on %B %d, %Y"
        )
