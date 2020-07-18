from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import sorting_algorithms


def script(request):
    algo = request.GET['data']
    n = request.GET['number']
    print(algo)
    print(n)
    print(type(algo))
    if int(algo) == 5:
        result = sorting_algorithms.merge(int(n))
    elif int(algo) == 3:
        result = sorting_algorithms.quick(int(n))
    elif int(algo) == 1:
        result = sorting_algorithms.bubble(int(n))
    elif int(algo) == 2:
        result = sorting_algorithms.insertion(int(n))
    return render(request, 'myvideo.html')
    

    


def index(request):
    return render(request, 'index.html')