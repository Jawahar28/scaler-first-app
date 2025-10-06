from rest_framework import serializers
from products.models import Product

class create_product_serializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100)
    # price = serializers.FloatField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields = ['name', 'price']