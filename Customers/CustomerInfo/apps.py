from django.apps import AppConfig


class CustomerinfoConfig(AppConfig):
    name = 'CustomerInfo'

    def ready(self):
        import CustomerInfo.signals