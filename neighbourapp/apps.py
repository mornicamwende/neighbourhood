from django.apps import AppConfig


class NeighbourappConfig(AppConfig):
    name = 'neighbourapp'

def ready(self):
        import users.signals
