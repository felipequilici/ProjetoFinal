from django.forms import ModelForm
from .models import (
    pessoa,
    veiculo,
    movimento_rotativo,
    mensalista,
)


class PessoaForm(ModelForm):
    class Meta:
        model = pessoa
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = veiculo
        fields = '__all__'

class MovrotForm(ModelForm):
    class Meta:
        model = movimento_rotativo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = mensalista
        fields = '__all__'

