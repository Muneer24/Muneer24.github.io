from django.apps import AppConfig

class BaseConfig(AppConfig):
    name = 'base'
    def ready(self):
        Products = self.get_model("Products")
        watson.register(Products)