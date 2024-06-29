
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from dashboard.serializers import CategorySerializer, ProductSerializer

from .models import Category, Product

# test view for dashboard
def dashboard(request):
    return HttpResponse("Dashboard view.")


# post view for product
@api_view(['POST'])
def postproduct(request):
    if request.method == 'POST':
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get view for all product
@api_view(['GET'])
def getAllProduct(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# get view for product by category
@api_view(['GET'])
def getProductByCategory(request, category):
    if request.method == 'GET':
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# post view for category
@api_view(['POST'])
def postcategory(request):
    if request.method == 'POST':
        category = request.data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# get view for all category
@api_view(['GET'])
def getAllCategory(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

# get view for product and category
@api_view(['GET'])
def allProductCategoryData(request):
    if request.method == 'GET':
        products = Product.objects.all()
        category = Category.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        category_serializer = CategorySerializer(category, many=True)
        return Response({'products': product_serializer.data, 'category': category_serializer.data})
    
    