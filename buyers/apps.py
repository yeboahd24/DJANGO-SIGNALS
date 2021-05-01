from django.apps import AppConfig


class BuyersConfig(AppConfig):
    name = 'buyers'

    def ready(self): # registering buyer singal
        import buyers.signals