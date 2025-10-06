from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.HellowView),
    path('hello/<str:name>/', views.HelloName),
    path('createProduct/', views.CreateProduct),
    
]