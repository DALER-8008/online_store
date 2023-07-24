from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StoreConfig(AppConfig):
    app_label = 'store'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.store'
    verbose_name = _('Store API')
