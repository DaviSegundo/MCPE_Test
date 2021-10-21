from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Process
from django.template import RequestContext

# Create your views here.

"""
Rota para fazer a construção do índice com todos os processos.
"""


def index(request):
    processos = Process.objects.all()

    form = RequestContext(request)
    if request.method == "POST":
        n_proc = request.POST['search']
        s_proc = Process.objects.filter(title=n_proc)
        procs = list()
        for p in s_proc:
            procs.append(p)
        return render(request, 'index.html', {'form': form, "processos_d": procs})

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
    cod = sorted(max)
    cod = cod[-1] + 1
    print(cod)

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
