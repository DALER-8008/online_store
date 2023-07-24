from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):
    app_label = 'orders'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
    verbose_name = _('Orders API')
