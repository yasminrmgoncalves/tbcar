from django.db import models
from math import ceil
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = 'Nome')
    endereco = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Endereço')
    complemento = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'complemento')
    bairro = models.CharField(max_length=50,blank= True, null = True, verbose_name = 'bairro')
    cidade = models.CharField(max_length = 50, blank = True, null = True, verbose_name = 'cidade')
    fone = models.CharField(max_length = 20, blank = True, null = True, verbose_name = 'telefone')
    email = models.EmailField(verbose_name = 'E-mail')
    foto = models.ImageField(upload_to = 'cliente_foto', blank = True, null = True, verbose_name = '')

    def __str__(self):
        return f"{self.nome} ({self.email})"

    
class Marca(models.Model):
    nome = models.CharField(max_length=30, verbose_name = 'Nome')
    url = models.URLField(verbose_name = 'Site', blank = True, null = True)
    logo = models.ImageField(upload_to='marca_logo', blank = True, null = True, verbose_name = '')

    def __str__(self):
        return self.nome



class Veiculo(models.Model):
    placa = models.CharField(max_length=8, verbose_name='Placa')
    modelo = models.CharField(max_length=30, blank = True, null = True, verbose_name='Modelo')
    cor = models.CharField(max_length=30, blank = True, null = True, verbose_name='Cor')
    marca_id = models.ForeignKey(Marca, on_delete = models.DO_NOTHING, verbose_name = 'Marca')
    ano = models.IntegerField(default = 2019, blank = True, null =True, verbose_name = 'Ano')
    cliente = models.ForeignKey(Cliente,  on_delete = models.DO_NOTHING, verbose_name = 'Cliente')
    fotoVeiculo = models.ImageField(upload_to= 'veiculo_foto', blank = True, null= True, verbose_name= '')

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

    class Meta:
        verbose_name_plural = 'Veículos'

class Tabela(models.Model):
    descricao = models.CharField(max_length=50, verbose_name = 'Descricao')
    valor = models.DecimalField(max_digits = 8, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    class Meta:
        verbose_name_plural = 'Tabelas'



class Mensalista(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete = models.CASCADE, verbose_name = 'Placa do Veiculo')
    id_tabela = models.ForeignKey(Tabela, on_delete = models.CASCADE, verbose_name = 'Valor do Veiculo')
    observacoes = models.TextField(blank=True, null = True, verbose_name = 'Observacoes')

    def __str__(self):
        return f"{self.id_veiculo} - {self.id_tabela}"

    class Meta:
        verbose_name_plural = 'Mensalistas'


class Rotativo(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete = models.CASCADE, verbose_name='Placa do Veiculo')
    id_tabela = models.ForeignKey(Tabela, on_delete = models.CASCADE, verbose_name='Id da Tabela')
    entrada = models.DateTimeField(auto_now= False, verbose_name='Entrada')
    saida = models.DateTimeField(auto_now = False, verbose_name='Saida')
    total = models.DecimalField(max_digits = 8, decimal_places=2, blank= True, null= True, verbose_name='Total')
    pago = models.BooleanField(default = False, verbose_name='Pago')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observacoes')

    def __str__(self):
        return f"{self.id_veiculo} - {self.id_tabela}: {self.entrada}"

    class Meta:
        verbose_name_plural = 'Rotativos'

    def calcula_total(self):
        if self.saida:
            hora = (self.saida - self.entrada).total_seconds()/3600
            obj = Tabela.objects.get(id=self.id_tabela.pk)
            if hora <= 0.5:
                self.total = obj.valor/2
            else:
                self.total = ceil(hora) * obj.valor
            return self.total
        else:
            return 0.0

