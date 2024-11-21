from django import forms
from .models import Cliente
from .models import Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cli_cpf',
            'cli_nome',
            'cli_email',
            'cli_tel',
            'cli_rua',
            'cli_numero',
            'cli_bairro',
            'cli_complemento',
            'cli_cidade',
            'cli_cep',
        ]
        widgets = {
            'cli_cpf': forms.TextInput(attrs={'placeholder': 'Digite o CPF'}),
            'cli_nome': forms.TextInput(attrs={'placeholder': 'Digite o nome'}),
            'cli_email': forms.EmailInput(attrs={'placeholder': 'Digite o email'}),
            'cli_tel': forms.TextInput(attrs={'placeholder': 'Digite o telefone'}),
            'cli_rua': forms.TextInput(attrs={'placeholder': 'Digite a rua'}),
            'cli_numero': forms.TextInput(attrs={'placeholder': 'Digite o número'}),
            'cli_bairro': forms.TextInput(attrs={'placeholder': 'Digite o bairro'}),
            'cli_complemento': forms.TextInput(attrs={'placeholder': 'Digite o complemento'}),
            'cli_cidade': forms.TextInput(attrs={'placeholder': 'Digite a cidade'}),
            'cli_cep': forms.TextInput(attrs={'placeholder': 'Digite o CEP'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'prod_nome',
            'prod_dsc',
            'prod_tipo',
            'prod_val',
            'prod_qntd',
        ]
        widgets = {
            'prod_nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do produto'}),
            'prod_dsc': forms.Textarea(attrs={'placeholder': 'Digite a descrição', 'rows': 3}),
            'prod_tipo': forms.TextInput(attrs={'placeholder': 'Digite o tipo do produto'}),
            'prod_val': forms.NumberInput(attrs={'placeholder': 'Digite o valor'}),
            'prod_qntd': forms.NumberInput(attrs={'placeholder': 'Digite a quantidade'}),
        }
