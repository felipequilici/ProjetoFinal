from django.forms import ModelForm
from .models import pessoa


class PessoaForm(ModelForm):
    class Meta:
        model = pessoa
        fields = '__all__'