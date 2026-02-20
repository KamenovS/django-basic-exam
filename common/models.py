from django.db import models

from common.mixins import TimeStampedModel
from companies.models import Offer, Company
from drivers.models import DriverAvailability


class OfferComment(TimeStampedModel):
    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    driver = models.ForeignKey(
        'drivers.Driver',
        on_delete=models.CASCADE
    )
    message = models.TextField()

    def __str__(self):
        return f'Comment by {self.driver.name}'


class AvailabilityComment(TimeStampedModel):
    availability = models.ForeignKey(
        DriverAvailability,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE
    )
    message = models.TextField()

    def __str__(self):
        return f'Comment by {self.company.name}'