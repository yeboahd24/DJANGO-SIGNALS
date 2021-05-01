from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self): # registering cars singal
        import cars.signals