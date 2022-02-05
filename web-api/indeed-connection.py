import os

from dotenv import load_dotenv
from indeed import IndeedClient

# wait on this https://pubwebapp.indeed.com/jobroll/traffic

load_dotenv()

indeed_client = os.getenv('indeedClient')

client = IndeedClient(publisher=indeed_client)

paramss = {
    'q': "python developer",
    'l': "Austin, TX",
    'sort': "date",
    'fromage': "5",
    'limit': "25",
    'filter': "1",
    'userip': "192.186.176.550:60409",
    'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}


def get_offers(params):
    # perform search
    search_results = client.search(**params)
    print(search_results)


get_offers(paramss)
