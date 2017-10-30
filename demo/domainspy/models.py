# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.utils import timezone


class Domain(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False,
    )
    domain = models.CharField(
        max_length=512,
        unique=True,
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
    )
    fetched = models.DateField(auto_now=True)
    title = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    keywords = models.TextField(blank=True, default="")
    address = models.TextField(blank=True, default="")
    phone_number = models.TextField(blank=True, default="")
    administrator = models.TextField(blank=True, default="")

    def __str__(self):
        return self.domain


class DomainRank(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False,
    )
    domain = models.ForeignKey(Domain)
    date = models.DateField(
        auto_now_add=True,
    )
    rank = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ("domain", "date"),
        )

    def __str__(self):
        return "{}: {}".format(self.domain, self.rank)


class Technology(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False,
    )
    text = models.CharField(
        max_length=512,
        unique=True,
    )

    def __str__(self):
        return self.text


class DomainTechnology(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False,
    )
    domain = models.ForeignKey(
        Domain,
        related_name='technologies',
    )
    technology = models.ForeignKey(
        Technology,
        related_name='domains',
    )

    class Meta:
        unique_together = (
            ("domain", "technology"),
        )

    def __str__(self):
        return "{}: {}".format(self.domain, self.technology)
