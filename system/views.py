from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Process
from django.template import RequestContext

# Create your views here.

"""
Rota para fazer a construção do índice com todos os processos.
"""


def index(request):
    processos = Process.objects.all().order_by("-created_date")

    form = RequestContext(request)

    return render(request, 'index.html', {'form': form, "processos_d": processos})


"""
Rota que redireciona para cada processo específico.
"""


def processos(request, processo_cod):
    processo = get_object_or_404(Process, pk=processo_cod)

    form = RequestContext(request)
    if request.method == "POST":
        processo.delete()
        return redirect('index')

    return render(request, 'processos.html', {'form': form, "processo": processo})


"""
Rota para fazer a criação de novos processos.
"""


def criar(request):
    # Gera uma pk nova com base nos indíces já registrados
    todos = Process.objects.all()
    max = list()
    for todo in todos:
        max.append(todo.cod)
    if len(max) == 0:
        max.append(1)
        cod = sorted(max)
        cod = cod[-1] + 1
    else:
        cod = sorted(max)
        cod = cod[-1] + 1

    # Passa as informações para gerar o select no html
    opts = Category.objects.all()

    # Estrutura de requisição do form
    form = RequestContext(request)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['categoria']
        category = Category.objects.filter(description=category)
        proc = Process.objects.create(
            cod=cod, title=title, description=description, category=category[0])
        proc.save()
        return redirect('index')

    return render(request, 'criar.html', {'form': form, 'opts': opts})


"""
Rota para fazer a alteração de dados do processo.
"""


def editar(request, processo_cod):
    processo = get_object_or_404(Process, pk=processo_cod)
    opts = Category.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        if title.isspace():
            title = "Sem Nome"
        description = request.POST['description']
        category = request.POST['categoria']
        category = request.POST['categoria']
        category = Category.objects.filter(description=category)

        Process.objects.filter(cod=processo_cod).update(title=title, description=description, category=category[0])
        return redirect('index')

    return render(request, 'editar.html', {'processo':processo, 'opts':opts})


"""
Rota para realizar a busca de processos dentre todos os cadastrados.
"""


def buscar(request):
    processos_busca = Process.objects.order_by("-created_date").filter()

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        processos_busca = processos_busca.filter(title__icontains=nome_buscar)
        
    return render(request, 'buscar.html', {'processos_d':processos_busca})
