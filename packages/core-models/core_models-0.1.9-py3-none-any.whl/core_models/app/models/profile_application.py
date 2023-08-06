from django.db import models

from .sector import Sector
from .country import Country
from .base import BaseModelAbstract
from ... import constants


class ProfileApplication(BaseModelAbstract, models.Model):
    company_name = models.CharField(max_length=255)
    company_registration_number = models.CharField(max_length=50)
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
    status = models.CharField(
        max_length=1,
        choices=constants.PROFILE_REQUEST_STATUSES,
        default=constants.PENDING_PROFILE_STATUS
    )

    def __unicode__(self):
        return self.company_name
