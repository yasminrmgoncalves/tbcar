from django.shortcuts import render, redirect
from core.forms import FormCliente, FormVeiculo, FormTabela, FormMensalista, FormRotativo, FormMarca
from core.models import Cliente, Marca, Veiculo, Tabela, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal') #não usa como entrada a url em si, mas o nome da url
    template_name = 'registration\\registrar.html'



def home(request):
    return render(request, 'core/index.html')

@login_required
def altera_cliente(request,id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
           if form.is_valid():
               form.save()
               messages.success(request, 'Dados do cliente alterados com sucesso')
               return redirect('url_lista_clientes')
        contexto = {'form': form, 'txt_titulo' : 'EditCliente', 'txt_descricao': 'Altera Cliente'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')

@login_required
def altera_veiculo(request,id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_lista_veiculos')
        contexto = {'form': form, 'txt_titulo' : 'EditVeiculo', 'txt_descricao' : 'Altera Veiculo'}
        return render(request, 'core/cadastro_veiculo.html', contexto)

    return render(request, 'core/aviso.html')

@login_required
def altera_tabela(request,id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormTabela(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_lista_tabelas')
        contexto = {'form': form, 'txt_titulo' : 'EditTabela', 'txt_descricao' : 'Altera Tabela'}
        return render(request, 'core/cadastro_tabela.html', contexto)

    return render(request, 'core/aviso.html')

@login_required # verifica se existe um usuário logado na tela
def cadastroCliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso')
            return redirect('url_lista_clientes')
        contexto = {'form': form, 'txt_titulo' : 'cad_cli', 'txt_descricao': 'Cadastro de Cliente'}
        return render(request, 'core/cadastro_cliente.html',contexto)
    return render(request, 'aviso.html')


@login_required
def listaClientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados':dados}
        return render(request, 'core/lista_clientes.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroVeiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'txt_titulo' : 'cad_veic', 'txt_descricao': 'Cadastro de Veiculo'}
        return render(request, 'core/cadastro_veiculo.html',contexto)
    return render(request, 'aviso.html')

@login_required
def listaVeiculos(request):
    dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculos.html', contexto)

def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    if request.POST:
        obj.delete()
        return redirect('url_lista_veiculos')
    else:
        contexto = {'txt_info': obj.placa}
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form' : form, 'txt_titulo' : 'cad_tab', 'txt_descricao' : 'Cadastro de Tabela'}
        return render(request, 'core/cadastro_tabela.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaTabelas(request):
    dados = Tabela.objects.all()
    contexto = {'dados': dados}
    return render (request,'core/lista_tabelas.html',contexto)


@login_required
def cadastroMensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form' : form, 'txt_titulo' : 'cad_mensa', 'txt_descricao' : 'Cadastro de Mensalista'}
        return render(request, 'core/cadastro_mensalista.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaMensalista(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados}
    return render (request,'core/lista_mensalista.html',contexto)

@login_required
def exclui_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    if request.POST:
        obj.delete()
        return redirect('url_lista_mensalista')
    else:
        contexto = {'txt_info': obj.id}
        return render(request, 'core/confirma_exclusao.html', contexto)

@login_required
def cadastroRotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form' : form, 'txt_titulo' : 'cad_rot', 'txt_descricao' : 'Cadastro de Rotativo'}
        return render(request, 'core/cadastro_rotativo.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaRotativo(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados}
    return render (request,'core/lista_rotativo.html',contexto)


@login_required
def altera_rotativo(request,id):
    obj = Rotativo.objects.get(id = id)
    form = FormRotativo(request.POST or None, instance=obj)
    if form.is_valid():
        obj.calcula_total()
        form.save()
        return redirect('url_lista_rotativo')
    else:
        contexto = {'form': form, 'txt_titulo': 'AltRot', 'txt_descricao': 'Altera Rotativo'}
        return render(request, 'core/cadastro.html', contexto)

@login_required
def exclui_rotativo(request, id_veiculo):
    obj = Rotativo.objects.get(id=id_veiculo)
    if request.POST:
        obj.delete()
        return redirect( 'url_lista_rotativo')
    else:
        contexto = {'txt_info': obj.id_veiculo}
        return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def cadastroMarca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form' : form, 'txt_titulo' : 'cad_marca', 'txt_descricao' : 'Cadastro de Marca'}
        return render(request, 'core/cadastro_marca.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaMarca(request):
    dados = Marca.objects.all()
    contexto = {'dados': dados}
    return render (request,'core/lista_marca.html',contexto)

@login_required
def altera_marca(request,id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_lista_marca')
        contexto = {'form': form, 'txt_titulo' : 'EditMarca', 'txt_descricao' : 'Altera Marca'}
        return render(request, 'core/cadastro_marca.html', contexto)

    return render(request, 'core/aviso.html')


@login_required
def exclui_marca(request, id):
    obj = Marca.objects.get(id=id)
    if request.POST:
        obj.delete()
        return redirect( 'url_lista_marca')
    else:
        contexto = {'txt_info': obj.id}
        return render(request, 'core/confirma_exclusao.html', contexto)