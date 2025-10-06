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
    print(p[0].name)
    return JsonResponse({'Hello' : name})

from products.create_product_serializer import create_product_serializer
from rest_framework.decorators import api_view  

@api_view(['POST'])
def CreateProduct(request):
    print(request.data)
    serializer = create_product_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    else:
        return JsonResponse(serializer.errors, status=400)
