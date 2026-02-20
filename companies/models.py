from django.db import models

from common.mixins import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    email = models.EmailField(
        unique=True,
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
    )
    address = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Offer(TimeStampedModel):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='offers'
    )
    title = models.CharField(
        max_length=100,)
    description = models.TextField()
    pickup_location = models.CharField(
        max_length=50,
    )
    delivery_location = models.CharField(
        max_length=50,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2)
    drivers = models.ManyToManyField(
        'drivers.Driver',
        blank=True,
        related_name='interested_offers'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']