import requests
from bs4 import BeautifulSoup
import csv

class Scraper:
    def get_webpage_html():
        website_url = 'https://www.goodreads.com/shelf/show/personal-development'
        r = requests.get(website_url)
        return r

    # TODO
    def parse_data(response_html):
        pass

    # TODO
    def write_to_csv(data):
        pass