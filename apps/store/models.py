from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils import shared, validators


class Store(shared.BaseModel):
    class Type(models.TextChoices):
        BRANCH = 'branch', 'Branch'
        MARKET = 'market', 'Market'
        POINT = 'point', 'Point'

    type = models.CharField(_('type'), max_length=30, choices=Type.choices, default=Type.MARKET)
    merchant = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='stores')
    phone = models.CharField(_('phone number'), max_length=15, unique=True, validators=[validators.phone_validator])
    address = models.CharField(_('address'), max_length=255)

    bank_name = models.CharField(_('bank name'), max_length=150)
    bank_id = models.CharField(_('bank id'), max_length=5)
    bank_account_number = models.CharField(_('bank account number'), max_length=10, unique=True)


class StoreAdmin(shared.BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='admins')
    admin = models.OneToOneField('users.User', on_delete=models.CASCADE)
