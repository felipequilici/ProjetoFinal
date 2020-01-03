from django.db import models
import  math

class pessoa(models.Model):
    nome = models.CharField(max_length=100)
    end = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    def __str__(self):
        return self.nome


class marca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class veiculo(models.Model):
    marca = models.ForeignKey(marca, on_delete=models.SET_NULL, null=True)
    dono = models.ForeignKey(pessoa, on_delete=models.SET_NULL, null=True)
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=30)
    cor = models.CharField(max_length=20)
    observacoes = models.TextField()
    def __str__(self):
        return self.modelo + " - " + self.placa + " - " + str(self.dono)


class parametro(models.Model):
    precohora = models.DecimalField(max_digits=5, decimal_places=2)
    mensalidade = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return "Parametros Gerais"


class movimento_rotativo(models.Model):
    entrada= models.DateTimeField(auto_now=False)
    saida= models.DateTimeField(auto_now=False, null=True)
    valor_hora=models.DecimalField(max_digits=5, decimal_places=2)
    veiculo= models.ForeignKey(veiculo, on_delete=models.SET_NULL, null=True)
    pago = models.BooleanField(default=False)

    def total_horas(self):
        return math.ceil((self.saida - self.entrada).total_seconds()/3600)

    def total(self):
        return self.valor_hora*self.total_horas()

    def __str__(self):
        return self.veiculo.placa


class mensalista(models.Model):
    veiculo= models.ForeignKey(veiculo, on_delete=models.SET_NULL, null=True)
    inicio = models.DateField()
    mensalidade = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.veiculo)


class MovimentosMensalista(models.Model):
    mensalista= models.ForeignKey(mensalista,on_delete=models.SET_NULL, null=True)
    dataPagamento = models.DateField()
    total = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.mensalista)