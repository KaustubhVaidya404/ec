from django.urls import path

from . import views


urlpatterns = [
    path('test', views.dashboard, name='dashboard'), # testing url
    path('postproduct', views.postproduct, name='postproduct'), # post product url
    path('postcategory', views.postcategory, name='postcategory'), # post category url
    path('getallproducts', views.getAllProduct, name='getallproducts'), # get all products url
    path('getproductbycategory/<str:category>', views.getProductByCategory, name='getproductbycategory'), # get product by category url
    path('getallcategory', views.getAllCategory, name='getallcategory'), # get all category url
    path('getallproductcategorydata', views.allProductCategoryData, name='getallproductcategorydata'), # get all product and category data url
]