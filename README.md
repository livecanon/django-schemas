Content Table

- [Requests](#requests)
- [Responses](#responses)
- [Views](#views)
- [Generic Views](#generic-views)

## [requests](https://www.django-rest-framework.org/api-guide/requests/)

```
    request.POST (django) ---> request.data (drf) (odpowiednik)
```

```
    request.GET (django) ---> request.query_params (drf) (odpowiednik)
```

```
    request.method
```

```
    request.content_type
```

## [responses](https://www.django-rest-framework.org/api-guide/responses/)

Unless you want to heavily customize REST framework for some reason, you should always use an **APIView** class or **@api_view** function for views that return **Response** objects.

_Signature_:

```
    Response(data, status=None, template_name=None, headers=None, content_type=None)
```

Remember: _data_ has to be serialized

## [Views](https://www.django-rest-framework.org/api-guide/views/)

Using the [**APIView**](https://www.cdrf.co/3.13/rest_framework.views/APIView.html) class is pretty much the same as using a regular **View** class, as usual, the incoming request is dispatched to an appropriate handler method such as **.get()** or **.post()**

_Example_

```
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

REST framework also allows you to work with regular function based views.

_Signature_:

```
    @api_view(http_method_names=['GET'])
```

The core of this functionality is the **api_view** decorator, which takes a list of HTTP methods that your view should respond to. For example, this is how you would write a very simple view that just manually returns some data:

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
```

## [Generic views](https://www.django-rest-framework.org/api-guide/generic-views/)

The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.
If the generic views don't suit the needs of your API, you can drop down to using the regular **APIView** class, or reuse the mixins and base classes used by the generic views to compose your own set of reusable generic views.

[**GenericAPIView**](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)

This class extends REST framework's **APIView** class, adding commonly required behavior for standard list and detail views.

Each of the concrete generic views provided is built by combining **GenericAPIView**, with one or more mixin classes.

**Mixins**:

The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as **.get()** and **.post()**, directly. This allows for more flexible composition of behavior.

The mixin classes can be imported from `rest_framework.mixins`.

- [ListModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#listmodelmixin)
- [CreateModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#createmodelmixin)
- [RetrieveModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#retrievemodelmixin)
- [UpdateModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#updatemodelmixin)
- [DestroyModelMixin](https://www.django-rest-framework.org/api-guide/generic-views/#destroymodelmixin)

**Concrete View Classes**:

If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.

The view classes can be imported from `rest_framework.generics`.

- [CreateAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#createapiview)
- [ListAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#listapiview)
- [RetrieveAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview)
- [DestroyAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#destroyapiview)
- [UpdateAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview)
- [ListCreateAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview)
- [RetrieveUpdateAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdateapiview)
- [RetrieveDestroyAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#retrievedestroyapiview)
- [RetrieveUpdateDestroyAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview)

**Save and deletion hooks**:

The following methods are provided by the mixin classes, and provide easy overriding of the object save or deletion behavior.

`perform_create(self, serializer)` - Called by **CreateModelMixin** when saving a new object instance.
`perform_update(self, serializer)` - Called by **UpdateModelMixin** when saving an existing object instance.
`perform_destroy(self, instance)` - Called by **DestroyModelMixin** when deleting an object instance.

These hooks are particularly useful for setting attributes that are implicit in the request, but are not part of the request data.

## [**serializers**](https://www.django-rest-framework.org/api-guide/serializers/)
