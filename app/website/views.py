from django.shortcuts import render


def index(request):
    context = {'selected': 'maps'}
    return render(request, 'website/index.html', context)

def table(request):
    context = {'selected': 'table'}
    return render(request, 'website/table.html', context)

def graphs(request):
    context = {'selected': 'graphs'}
    return render(request, 'website/graphs.html', context)

def api(request):
    context = {'selected': 'api'}
    return render(request, 'website/api.html', context)
