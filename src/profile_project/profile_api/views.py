from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView (APIView):
    """" Test API views """""
    def get (self, request, format = None):
        """" Returns a list of features """""
        an_apiview = [ 'An API view uses HTTP methods as functions (get, post, patch, put, delete)',
        'It is similar to a traditional django view',
        'It gives control over the logic',
        'It maps manually to URLs']
        return Response ({'message' : 'Hello', 'an_apiview' : an_apiview})
