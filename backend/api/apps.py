from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .tasks import start
        start()


# https://medium.com/@canadiyaman/how-to-use-firebase-with-django-project-34578516bafe
