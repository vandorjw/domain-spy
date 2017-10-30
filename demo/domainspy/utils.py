# -*- coding: utf-8 -*-
import logging
from bs4 import BeautifulSoup
import requests
from django.conf import settings as dj_settings

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def scrape(url):
    if django_settings.USE_PUPPETEER:
        url = dj_settings.PUPPETEER_PROXY + "?url=" + url
        r = requests.get(url, auth=(dj_settings.PUPPETEER_USER, dj_settings.PUPPETEER_PASSWORD))
    else:
        r = requests.get(url)

    if r.status_code == 200:
        return r.text
    else:
        logging.debug(r.status_code)
        return ""


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
