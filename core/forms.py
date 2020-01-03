from django.forms import ModelForm
from .models import (
    pessoa,
    veiculo,
)


class PessoaForm(ModelForm):
    class Meta:
        model = pessoa
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = veiculo
        fields = '__all__'