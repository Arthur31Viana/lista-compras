from django.apps import AppConfig

#Personalizar area do nome da tabela no DB
class CoreConfig(AppConfig):
    name = 'comprex.core'
    verbose_name = 'Cadastros'
