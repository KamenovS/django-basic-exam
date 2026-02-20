from django.db import models

from common.mixins import TimeStampedModel
from drivers.choices import DriverCategoryChoices, TrailerTypeChoices


class Driver(TimeStampedModel):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    phone = models.CharField(
        max_length=15,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    category = models.CharField(
        max_length=20,
        choices=DriverCategoryChoices.choices
    )
    trailer_type = models.CharField(
        max_length=20,
        choices=TrailerTypeChoices.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class DriverAvailability(TimeStampedModel):
    driver = models.ForeignKey(
        'Driver',
        on_delete=models.CASCADE,
        related_name='availabilities'
    )
    current_location = models.CharField(
        max_length=50,
    )
    available_from = models.DateField()
    description = models.TextField()
    companies = models.ManyToManyField(
        'companies.Company',
        blank=True,
        related_name='interested_drivers',
    )

    def __str__(self):
        return f'{self.driver.name} - {self.current_location}'

    class Meta:
        ordering = ['-created_at']