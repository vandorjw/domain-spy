# -*- coding: utf-8 -*-
import json
import logging
from django.shortcuts import get_object_or_404
from .models import Domain
from .models import DomainURI
from .models import DomainRank
from .models import Technology
from .models import DomainTechnology
from .serializers import DomainSerializer
from .serializers import DomainURISerializer
from .serializers import DomainRankSerializer
from .serializers import TechnologySerializer
from .serializers import DomainTechnologySerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from domainspy import tasks

from .utils import HTMLParser
from .utils import url_to_domain

logger = logging.getLogger(__name__)


class DomainViewSet(viewsets.ModelViewSet):
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()


class DomainURIViewSet(viewsets.ModelViewSet):
    serializer_class = DomainURISerializer
    queryset = DomainURI.objects.all()


class DomainRankViewSet(viewsets.ModelViewSet):
    serializer_class = DomainRankSerializer
    queryset = DomainRank.objects.all()


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()


class DomainTechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = DomainTechnologySerializer
    queryset = DomainTechnology.objects.all()


@api_view(['GET'], )
def fetch_domain_details(request):
    url = request.query_params.get('url')
    domain = url_to_domain(url)
    if domain:
        tasks.scrape.delay(url)
        domain_obj, created = Domain.objects.get_or_create(domain=domain)
        serializer = DomainSerializer(domain_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST',])
def crawl(request):
    try:
        body = request.body.decode('utf-8')
        payload = json.loads(body)
        url = payload.get('url')
        domain = url_to_domain(url)
        domain_obj, created = Domain.objects.get_or_create(domain=domain)
        html_doc = scrape(url)
        parser = HTMLParser(html_doc)
        title = parser.get_meta_title()
        description = parser.get_meta_description()
        return Response({"title": title, "description": description}, status=status.HTTP_200_OK)
    except Exception as err:
        logger.error(err)
        return Response({"error": 'Error crawling URI'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
