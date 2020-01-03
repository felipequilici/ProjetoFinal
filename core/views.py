from django.shortcuts import render, redirect
from django.http import HttpResponse

from core.models import (
    pessoa,
    veiculo,
    movimento_rotativo,
    mensalista,
    MovimentosMensalista)
from .forms import (
    PessoaForm,
    VeiculoForm,
)


def home(request):
    context = {'mensagem': 'Olá mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = pessoa.objects.all()
    form= PessoaForm()
    data= {'pessoas': pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def lista_veiculos(request):
    veiculos = veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def lista_movrot(request):
    movrot = movimento_rotativo.objects.all()
    return render(request, 'core/lista_movrot.html', {'movrot': movrot})

def lista_mensalistas(request):
    mensalistas = mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})

def lista_movmen(request):
    movmen = MovimentosMensalista.objects.all()
    return render(request, 'core/lista_movmen.html', {'movmen': movmen})


