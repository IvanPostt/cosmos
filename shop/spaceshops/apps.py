from django.apps import AppConfig


class SpaceshopsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spaceshops'

    def ready(self):
        import spaceshops.translation
