from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .models import Cliente, Produto
from .forms import ClienteForm, ProdutoForm

def index(request):
    return redirect('listar')

def listar(request):
    # Busca todos os clientes e produtos
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    # Retorna os dados para o template 'listar.html'
    return render(request, 'listar.html', {'clientes': clientes, 'produtos': produtos})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')  # Redireciona para a lista de clientes após salvar
    else:
        form = ClienteForm()  # Cria um formulário vazio

    # Retorna o formulário para o template 'adicionar_cliente.html'
    return render(request, 'adicionar_cliente.html', {'form': form})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')  # Redireciona para a lista de produtos após salvar
    else:
        form = ProdutoForm()  # Cria um formulário vazio

    # Retorna o formulário para o template 'adicionar_produto.html'
    return render(request, 'adicionar_produto.html', {'form': form})

def editar_cliente(request, cpf):
    cliente = get_object_or_404(Cliente, cli_cpf=cpf)  # Busca o cliente pelo CPF
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()  # Salva o cliente editado
            return redirect('listar')  # Redireciona para a lista após editar
    else:
        form = ClienteForm(instance=cliente)  # Carrega os dados do cliente no formulário

    return render(request, 'editar_cliente.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, prod_id=id)  # Busca o produto pelo ID
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()  # Salva o produto editado
            return redirect('listar')  # Redireciona para a lista após editar
    else:
        form = ProdutoForm(instance=produto)  # Carrega os dados do produto no formulário

    return render(request, 'editar_produto.html', {'form': form})

def deletar_cliente(request, cpf):
    cliente = get_object_or_404(Cliente, cli_cpf=cpf)  # Busca o cliente pelo CPF
    if request.method == 'POST':
        cliente.delete()  # Deleta o cliente
        return redirect('listar')  # Redireciona para a lista após deletar
    return render(request, 'confirmar_delecao_cliente.html', {'obj': cliente})  # Solicita confirmação de exclusão

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, prod_id=id)  # Busca o produto pelo ID
    if request.method == 'POST':
        produto.delete()  # Deleta o produto
        return redirect('listar')  # Redireciona para a lista após deletar
    return render(request, 'confirmar_delecao.html', {'obj': produto})  # Solicita confirmação de exclusão

def page_not_found(request, exception):
    return render(request, '404.html', status=404)  # Página de erro 404 personalizada
