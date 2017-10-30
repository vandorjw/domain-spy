# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from .models import Domain
from .models import DomainRank
from .models import Technology
from .models import DomainTechnology
from .serializers import DomainSerializer
from .serializers import DomainRankSerializer
from .serializers import TechnologySerializer
from .serializers import DomainTechnologySerializer
from rest_framework import viewsets
from rest_framework.response import Response


class DomainViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving domain data.
    """
    def list(self, request):
        queryset = Domain.objects.all()
        serializer = DomainSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Domain.objects.all()
        domain = get_object_or_404(queryset, pk=pk)
        serializer = DomainSerializer(domain)
        return Response(serializer.data)
