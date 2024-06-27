
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from dashboard.serializers import CategorySerializer, ProductSerializer


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