from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.serializers import ProductSerializer
from product.service.product_service import ProductService


class ProductListCreateView(APIView):
    def get(self, request):
        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = ProductService.create_product(**serializer.validated_data)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)