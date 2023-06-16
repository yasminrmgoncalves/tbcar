"""TBCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, cadastroCliente, listaClientes, cadastroVeiculo, listaVeiculos, cadastroTabela, listaTabelas, Registrar,altera_cliente, altera_veiculo, altera_tabela, cadastroMensalista, cadastroRotativo, listaMensalista, listaRotativo
from core.views import exclui_veiculo, exclui_rotativo, exclui_mensalista, altera_rotativo, cadastroMarca, listaMarca, altera_marca, exclui_marca
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name ="url_registrar"),
    path('captcha/', include('captcha.urls')),
    path('', home, name = 'url_principal'),
    path('cadastro_cliente/', cadastroCliente, name = "url_cadastro_cliente"),
    path('lista_clientes/', listaClientes, name = "url_lista_clientes"),
    path('alterar_cliente/<int:id>/', altera_cliente, name = 'url_altera_cliente'),
    path('cadastro_veiculo/', cadastroVeiculo, name = "url_cadastro_veiculo"),
    path('lista_veiculos/', listaVeiculos, name = "url_lista_veiculos"),
    path('alterar_veiculo/<int:id>/', altera_veiculo, name = 'url_altera_veiculo'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('cadastro_tabela/', cadastroTabela, name = "url_cadastro_tabela"),
    path ('lista_tabelas/', listaTabelas, name = "url_lista_tabelas"),
    path ('alterar_tabela/<int:id>/', altera_tabela, name = "url_altera_tabela"),
    path('cadastro_mensalista/',cadastroMensalista, name = "url_cadastro_mensalista" ),
    path('cadastro_rotativo/',cadastroRotativo, name = "url_cadastro_rotativo" ),
    path('lista_mensalista/',listaMensalista, name = "url_lista_mensalista" ),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('lista_rotativo/',listaRotativo, name = "url_lista_rotativo" ),
    path('alterar_rotativo/<int:id>/', altera_rotativo, name = "url_altera_rotativo"),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),
    path('cadastro_marca/', cadastroMarca, name = "url_cadastro_marca"),
    path('lista_marca/', listaMarca, name = "url_lista_marca"),
    path ('alterar_marca/<int:id>/', altera_marca, name = "url_altera_marca"),
    path('exclui_marca/<int:id>/', exclui_marca, name='url_exclui_marca'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)