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
    movrot_novo,
    mensalista_novo,
    movmen_novo,
    pessoa_update,
    veiculo_update,
    mensalista_update,
    movrot_update,
    movmen_update,
    pessoa_delete,
    veiculo_delete,
)


urlpatterns = [
    re_path('^$', home, name='core_home'),
    re_path('^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path('^pessoas-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoas-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoas-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    re_path('^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path('^veiculos-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculos-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculos-delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),

    re_path('^movrot/$', lista_movrot, name='core_lista_movrot'),
    re_path('^movrot-novo/$', movrot_novo, name='core_movrot_novo'),
    re_path(r'^movrot-update/(?P<id>\d+)/$', movrot_update, name='core_movrot_update'),

    re_path('^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path('^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),

    re_path('^movmen/$', lista_movmen, name='core_lista_movmen'),
    re_path('^movmen-novo/$', movmen_novo, name='core_movmen_novo'),
    re_path(r'^movmen-update/(?P<id>\d+)/$', movmen_update, name='core_movmen_update'),
]




