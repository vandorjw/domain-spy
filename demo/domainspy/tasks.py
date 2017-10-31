from celery import shared_task
import requests
from django.conf import settings as dj_settings
from .models import Domain, DomainURI
from .utils import url_to_domain
from .utils import url_to_path
from .utils import HTMLParser


@shared_task
def scrape(url):
    domain = url_to_domain(url)
    path = url_to_path(url)
    domain_obj, created = Domain.objects.get_or_create(
        domain=domain)
    domain_uri_obj, created = DomainURI.objects.get_or_create(
        domain=domain_obj, uri=path)
    if dj_settings.USE_PUPPETEER:
        url = dj_settings.PUPPETEER_PROXY + "?url=" + url
        r = requests.get(url, auth=(dj_settings.PUPPETEER_USER, dj_settings.PUPPETEER_PASSWORD))
    else:
        r = requests.get(url)

    if r.status_code == 200:
        html_doc = r.text
        parser = HTMLParser(html_doc)
        domain_uri_obj.title = parser.get_meta_title()
        domain_uri_obj.description = parser.get_meta_description()
        domain_uri_obj.keywords = parser.get_meta_keywords()
        domain_uri_obj.save()
        return "success"
    else:
        return "failed"
