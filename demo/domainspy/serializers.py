# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Domain
from .models import DomainRank
from .models import Technology
from .models import DomainTechnology


class DomainSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(label='ID', read_only=True)
    class Meta:
        model = Domain
        fields = (
            'uuid',
            'domain',
            'parent',
            'fetched',
            'title',
            'description',
            'keywords',
            'address',
            'phone_number',
            'administrator',
        )


class DomainRankSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(label='ID', read_only=True)
    class Meta:
        model = DomainRank
        fields = (
            'uuid',
            'domain',
            'date',
            'rank',
        )


class TechnologySerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(label='ID', read_only=True)
    class Meta:
        model = Technology
        fields = (
            'uuid',
            'text',
        )


class DomainTechnologySerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(label='ID', read_only=True)
    class Meta:
        model = Technology
        fields = (
            'uuid',
            'domain',
            'technology',
        )
