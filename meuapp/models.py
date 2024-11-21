from django.db import models

class Cliente(models.Model):
    cli_cpf = models.CharField(max_length=11, primary_key=True)  # CPF tem 11 caracteres
    cli_nome = models.CharField(max_length=255)  # Nome do cliente
    cli_tel = models.CharField(max_length=15)  # Número de telefone
    cli_rua = models.CharField(max_length=255)  # Rua
    cli_numero = models.CharField(max_length=10)  # Número da residência
    cli_bairro = models.CharField(max_length=100)  # Bairro
    cli_complemento = models.CharField(max_length=100, blank=True, null=True)  # Complemento opcional
    cli_cidade = models.CharField(max_length=100)  # Cidade
    cli_cep = models.CharField(max_length=8)  # CEP (formatado sem traços)
    cli_email = models.EmailField(max_length=255)  # E-mail do cliente

    def __str__(self):
        return self.cli_nome  # Retorna o nome do cliente como string

    class Meta:
        managed = False  # Django não gerencia essa tabela
        db_table = 'cliente'  # Nome exato da tabela no banco de dados

class Produto(models.Model):
    prod_id = models.AutoField(primary_key=True)  # ID auto incremental do produto
    prod_nome = models.CharField(max_length=255)  # Nome do produto
    prod_dsc = models.TextField()  # Descrição do produto
    prod_tipo = models.CharField(max_length=50)  # Tipo do produto
    prod_val = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do produto
    prod_qntd = models.IntegerField()  # Quantidade do produto em estoque

    def __str__(self):
        return self.prod_nome  # Retorna o nome do produto como string

    class Meta:
        managed = False  # Django não gerencia essa tabela
        db_table = 'produto'  # Nome exato da tabela no banco de dados

