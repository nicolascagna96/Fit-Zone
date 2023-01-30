from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Plan(models.Model):
    """Model for the workout request service"""
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    your_goal = models.TextField(
        max_length=254, null=False, blank=False, default='')
    PLAN_CHOICES = [
        ('Gym', 'Gym'),
        ('Home', 'Home'),
        ('Outdoor', 'Outdoor'),

    ]
    plan_type = models.CharField(
        max_length=40,
        choices=PLAN_CHOICES,
        default='Gym',
    )

    def save(self, *args, **kwargs):
        super(Plan, self).save(*args, **kwargs)
