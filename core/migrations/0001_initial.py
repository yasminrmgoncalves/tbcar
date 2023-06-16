# Generated by Django 4.1.7 on 2023-03-17 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='cidade')),
                ('fone', models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='cliente_foto', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Site')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='marca_logo', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('modelo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Modelo')),
                ('cor', models.CharField(blank=True, max_length=30, null=True, verbose_name='Cor')),
                ('ano', models.IntegerField(blank=True, default=2019, null=True, verbose_name='Ano')),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.marca', verbose_name='Marca')),
            ],
        ),
    ]