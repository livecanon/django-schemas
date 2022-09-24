from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [path("", views.api_home), path("products/", include("products.urls"))]
