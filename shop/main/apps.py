from django.apps import AppConfig


class MainConfig(AppConfig):
    verbose_name = 'Космос'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        import main.translation
