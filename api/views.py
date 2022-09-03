from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms import model_to_dict

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def products_view(request):
    instance = Product.objects.all().order_by('?').first()
    # instance = Product.objects.all()
    # data = {}
    # for product in products:
    #     data[product.id] = model_to_dict(product)
    data = ProductSerializer(instance).data
    # data['params'] = request.GET
    # data['body'] = json.loads(request.body)


    return Response(data)
    