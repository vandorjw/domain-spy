# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import DomainViewSet
from .views import DomainURIViewSet
from .views import DomainRankViewSet
from .views import TechnologyViewSet
from .views import DomainTechnologyViewSet
from .views import fetch_domain_details
from .views import crawl

router = DefaultRouter()
router.register(r'domains', DomainViewSet)
router.register(r'uris', DomainURIViewSet)
router.register(r'ranks', DomainRankViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'domaintechnologies', DomainTechnologyViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^fetch/$', fetch_domain_details),
    url(r'^crawl/$', crawl),
]
