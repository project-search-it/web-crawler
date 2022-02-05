import requests
import re
from bs4 import BeautifulSoup

from jobs import Job

job_types = []


def job_scraper(search_query) -> list[Job]:
    returned_jobs = []

    session = requests.Session()
    response = session.get('https://www.indeed.com/jobs?q={}'.format(search_query),
                           headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ('
                                                  'KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'})

    soup = BeautifulSoup(response.text, 'html.parser')

    find_page_count(soup)

    return returned_jobs


def find_page_count(session) -> list[str]:
    page_count = 0
    page_elements = session.findAll("span", {"class": re.compile(r'pn')})

    pages_found = []

    for element in page_elements:
        pages_found.append(element.text)

    pages_formatted = []

    for i in range(len(pages_found)):
        if page_count == 0:
            pages_formatted.append('00')
            page_count += 10

        pages_formatted.append(str(page_count))
        page_count += 10

    return pages_formatted

