from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def HellowView(request):
    print(request.method)
    print(request.headers)
    return JsonResponse({"hello" : "World!"})

def HelloName(request, name):
    print(name)
    return JsonResponse({'Hello' : name})
