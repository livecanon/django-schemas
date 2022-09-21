### [requests](https://www.django-rest-framework.org/api-guide/requests/)

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

### [responses](https://www.django-rest-framework.org/api-guide/responses/)

Unless you want to heavily customize REST framework for some reason, you should always use an **APIView** class or **@api_view** function for views that return Response objects.

```
    Response(data, status=None, template_name=None, headers=None, content_type=None)
```

Remember: data has to be serialized

### [Views](https://www.django-rest-framework.org/api-guide/views/)

REST framework provides an APIView class, which subclasses Django's View class.

_Example_

```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

REST framework also allows you to work with regular function based views.

```
    Signature: @api_view(http_method_names=['GET'])
```

The core of this functionality is the api_view decorator, which takes a list of HTTP methods that your view should respond to. For example, this is how you would write a very simple view that just manually returns some data:

```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
```
