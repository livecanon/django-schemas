from django.http import JsonResponse
import json
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # --- One way of doing this:
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        # --- or
        data = model_to_dict(model_data, fields=["id", "title"])
    return Response(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # --- One way of doing this:
#         # data["title"] = model_data.title
#         # data["content"] = model_data.content
#         # data["price"] = model_data.price
#         # --- or
#         data = model_to_dict(model_data, fields=["id", "title"])
#         # Flow
#         # model instance (model_data)
#         # turn a Python dict
#         # return JSON to my client
#     return JsonResponse(data)
