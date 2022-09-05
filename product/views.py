from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
        data = serializer.data
        return Response(data)

@api_view(['GET'])
def products_view(request):
    # instance = Product.objects.all().order_by('?').first()
    queryset = Product.objects.all()
    # data = {}
    # for product in products:
    #     data[product.id] = model_to_dict(product)
    data = ProductSerializer(queryset, many=True).data
    # data['params'] = request.GET
    # data['body'] = json.loads(request.body)


    return Response(data)
    

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer