from django.db import models

from .sector import Sector
from .country import Country
from .base import BaseModelAbstract


class ProfileApplication(BaseModelAbstract, models.Model):
    company_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=25)
    country = models.ForeignKey(
        Country, models.SET_NULL, null=True, blank=True
    )
    sector = models.ForeignKey(Sector, models.SET_NULL, null=True, blank=True)
    export_countries = models.TextField()
    largest_buyers = models.TextField()
    annual_turnover = models.DecimalField(
        decimal_places=2, max_digits=30,
        null=False, blank=False
    )
    status = models.CharField(max_length=1, choices=[], default='')
