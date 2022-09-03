from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # adding more fields to the models
    description = serializers.SerializerMethodField(read_only=True)
    sale_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'sale_price'
        ]
    
    def get_description(self, obj):
        return obj.content
    
    def get_sale_price(self, obj):
        # coupoun discount logic
        return '%.2f' %(float(obj.price) * 0.8)
