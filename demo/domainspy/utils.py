# -*- coding: utf-8 -*-
import logging
import re
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def url_to_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain


def url_to_path(url):
    parsed_uri = urlparse(url)
    path = '{uri.path}'.format(uri=parsed_uri)
    return path


def get_alexa_rank(domain):
    url = "https://data.alexa.com/data?cli=10&dat=snbamz&url=" + domain
    r = requests.get(url)
    if r.status_code == 200:
        tree = ET.fromstring(r.content)
        sd1, sd2 = tree.findall('SD')
        popularity = sd2.find('POPULARITY')
        rank = popularity.get('TEXT')
        return int(rank)


class HTMLParser(object):

    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def get_meta_title(self):
        try:
            return self.soup.title.string
        except Exception as err:
            logger.error(err)
            return ""

    def get_meta_description(self):
        description_element = self.soup.find(attrs={"name":"description"})
        try:
            return description_element['content']
        except Exception as err:
            logger.error(err)
            return ""

    def get_meta_keywords(self):
        keywords_element = self.soup.find(attrs={"name":"keywords"})
        try:
            return keywords_element['content']
        except Exception as err:
            logger.error(err)
            return ""

    def get_facebook_handle(self):
        return ""

    def get_twitter_handle(self):
        return ""

    def get_google_plus_handle(self):
        return ""

    def get_alexa_global_rank(self):
        traffic_rank_content = self.soup.find("section", {"id": "traffic-rank-content"})
        page_ranks = traffic_rank_content.find_all("strong", {"class": "metrics-data"})
        try:
            global_rank = page_ranks[0].text
            rank = re.sub('[^0-9]','', global_rank)
            return int(rank)
        except Exception as err:
            logger.error(err)
            return None
