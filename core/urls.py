from django.contrib import admin
from django.urls import re_path, include
from .views import(
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrot,
    lista_mensalistas,
    lista_movmen,
    pessoa_novo,
    veiculo_novo,
)


urlpatterns = [
    re_path('^$', home, name='core_home'),
    re_path('^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path('^pessoas-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path('^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path('^veiculos-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path('^movrot/$', lista_movrot, name='core_lista_movrot'),
    re_path('^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path('^movmen/$', lista_movmen, name='core_lista_movmen'),
]
