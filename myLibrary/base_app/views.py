from django.shortcuts import render
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

# Create your views here.

class APIRootView(APIView):
    """
    Root view with all the endpoints of the API
    """
    _ignore_model_permissions = True
    exclude_from_schema = True
    swagger_schema = None

    def get_view_name(self):
        return "API Root"

    def get(self, request, format=None):
        return Response(OrderedDict((
            ('books', reverse('books-api:api-root', request=request, format=format)),
        )))