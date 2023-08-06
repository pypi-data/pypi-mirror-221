import os

from django.db import models
from django.utils import timezone

from .sector import Sector
from .country import Country, Region, City
from .base import BaseModelAbstract
from .user import User


class Company(BaseModelAbstract, models.Model):
    created_by = None
    user = models.OneToOneField(User, models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, models.SET_NULL, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    annual_turnover = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    address_line1 = models.TextField(null=True, blank=True)
    address_line2 = models.TextField(null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    region = models.ForeignKey(Region, models.SET_NULL, blank=True, null=True, verbose_name="Region/State")
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_verified = models.DateTimeField(null=True, blank=True)

    @property
    def address(self):
        return f"{self.address_line1}, {self.city}, {self.region}, {self.country}"

    class Meta:
        verbose_name_plural = 'Companies'

    def save(self, keep_deleted=False, **kwargs):
        self.date_verified = timezone.now() if self.is_verified else None
        super(Company, self).save(keep_deleted, **kwargs)

    def __unicode__(self):
        return f"{self.name}|{self.registration_number}|{self.is_verified}"


def doc_upload_to(instance, filename):
    f, ext = os.path.splitext(filename)
    return f'company-docs/{instance.id}{ext}'


class CompanyDocument(BaseModelAbstract, models.Model):
    company = models.ForeignKey(Company, models.CASCADE, related_name='docs')
    file = models.FileField(null=False, blank=False, upload_to=doc_upload_to)
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Company Document"
        verbose_name_plural = "Company Documents"

    def __unicode__(self):
        return f"{self.company.name} - {self.name}"
