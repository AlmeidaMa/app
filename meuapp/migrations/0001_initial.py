# Generated by Django 5.1.3 on 2024-11-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('cli_nome', models.CharField(max_length=255)),
                ('cli_tel', models.CharField(max_length=15)),
                ('cli_rua', models.CharField(max_length=255)),
                ('cli_numero', models.CharField(max_length=10)),
                ('cli_bairro', models.CharField(max_length=100)),
                ('cli_complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('cli_cidade', models.CharField(max_length=100)),
                ('cli_cep', models.CharField(max_length=8)),
                ('cli_email', models.EmailField(max_length=255)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_nome', models.CharField(max_length=255)),
                ('prod_dsc', models.TextField()),
                ('prod_tipo', models.CharField(max_length=50)),
                ('prod_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prod_qntd', models.IntegerField()),
            ],
            options={
                'db_table': 'produto',
                'managed': False,
            },
        ),
    ]