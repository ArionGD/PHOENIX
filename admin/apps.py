from django.apps import AppConfig

class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin'
    label = 'phoenix_admin' # Special label to keep it distinct from django.contrib.admin
