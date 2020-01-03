from django.shortcuts import render
from django.http import HttpResponse

from core.models import (
    pessoa,
    veiculo,
    movimento_rotativo,
    mensalistas,
    MovimentosMensalista)


def home(request):
    context = {'mensagem':'Olá mundo'}
    return  render (request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})

def lista_veiculos(request):
    veiculos = veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})

def lista_movrot(request):
    movrot = movimento_rotativo.objects.all()
    return render(request, 'core/lista_movrot.html', {'movrot': movrot})

def lista_mensalistas(request):
    mensalistas = mensalistas.objects.all()
    return render(request, 'core/lista_movrot.html', {'mensalistas': mensalistas})

def lista_movrot(request):
    movmen = MovimentosMensalista.objects.all()
    return render(request, 'core/lista_movrot.html', {'movmen': movmen})
