from django.shortcuts import render, redirect
from django.http import HttpResponse

from core.models import (
    pessoa,
    veiculo,
    movimento_rotativo,
    mensalista,
    MovimentosMensalista,
)
from .forms import (
    PessoaForm,
    VeiculoForm,
    MovrotForm,
    MensalistaForm,
    MovmenForm
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

def pessoa_update(request, id):
    data= {}
    Pessoa = pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=Pessoa)
    data['pessoa'] = Pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    Pessoa = pessoa.objects.get(id=id)
    if request.method=='POST':
        Pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_delete.html', {'pessoa':Pessoa})



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

def veiculo_update(request, id):
    data= {}
    Veiculo = veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=Veiculo)
    data['veiculo'] = Veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)

def veiculo_delete(request, id):
    Veiculo = veiculo.objects.get(id=id)
    if request.method=='POST':
        Veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_delete.html', {'veiculo':Veiculo})

def lista_movrot(request):
    movrot = movimento_rotativo.objects.all()
    form = MovrotForm()
    data = {'movrot': movrot, 'form': form}
    return render(request, 'core/lista_movrot.html', data)

def movrot_novo(request):
    form = MovrotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrot')

def movrot_update(request, id):
    data= {}
    Rot = movimento_rotativo.objects.get(id=id)
    form = MovrotForm(request.POST or None, instance=Rot)
    data['movrot'] = Rot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrot')
    else:
        return render(request, 'core/update_movrot.html', data)

def movrot_delete(request, id):
    movrot = movimento_rotativo.objects.get(id=id)
    if request.method=='POST':
        movrot.delete()
        return redirect('core_lista_movrot')
    else:
        return render(request, 'core/movrot_delete.html', {'movrot':movrot})

def lista_mensalistas(request):
    mensalistas = mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def mensalista_update(request, id):
    data= {}
    Mensalista = mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=Mensalista)
    data['mensalista'] = Mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)

def mensalista_delete(request, id):
    Mensalista = mensalista.objects.get(id=id)
    if request.method=='POST':
        Mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalista_delete.html', {'mensalista':Mensalista})

def lista_movmen(request):
    movmen = MovimentosMensalista.objects.all()
    form = MovmenForm()
    data = {'movmen': movmen, 'form': form}
    return render(request, 'core/lista_movmen.html', data)

def movmen_novo(request):
    form = MovmenForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmen')

def movmen_update(request, id):
    data= {}
    Men = MovimentosMensalista.objects.get(id=id)
    form = MovmenForm(request.POST or None, instance=Men)
    data['movmen'] = Men
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmen')
    else:
        return render(request, 'core/update_movmen.html', data)

def movmen_delete(request, id):
    movmen = MovimentosMensalista.objects.get(id=id)
    if request.method=='POST':
        movmen.delete()
        return redirect('core_lista_movmen')
    else:
        return render(request, 'core/movmen_delete.html', {'movmen':movmen})