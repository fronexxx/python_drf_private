from django.core import validators as V
from django.db import models

from core.constants.choices import StatusChoices
from core.enums.regex_enum import RegexEnum
from core.models import BaseModel


class ContactModel(BaseModel):
    class Meta:
        db_table = 'contacts'

    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, validators=[V.RegexValidator(RegexEnum.PHONE_NUMBER.pattern, RegexEnum.PHONE_NUMBER.msg)])
    company = models.CharField(max_length=20)
    status = models.CharField(max_length=9, choices=StatusChoices, default=StatusChoices.NEW)
