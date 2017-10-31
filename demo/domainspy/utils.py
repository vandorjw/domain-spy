# -*- coding: utf-8 -*-
import logging
from urllib.parse import urlparse
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
