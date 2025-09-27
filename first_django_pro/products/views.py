from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from products.models import Product

def HellowView(request):
    print(request.method)
    print(request.headers)
    
    return JsonResponse({"hello" : "World!"})

def HelloName(request, name):
    p = Product.objects.all()
    print(p)
    return JsonResponse({'Hello' : name})
