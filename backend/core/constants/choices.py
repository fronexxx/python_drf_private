from django.db import models

class StatusChoices(models.TextChoices):
    NEW = 'New'
    CONTACTED = 'Contacted'
    CUSTOMER = 'Customer'