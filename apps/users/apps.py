from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    app_label = 'users'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    verbose_name = _('Users API')
