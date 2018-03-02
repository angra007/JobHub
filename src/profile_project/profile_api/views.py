from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloAPIView (APIView):
    """" Test API views """""

    serializer_class = serializers.HelloSerializer

    def post (self, request) :
        """" Create a hellp message with our name """""
        serializer = serializers.HelloSerializer (data = request.data)
        if serializer.is_valid ():
            name = serializer.data.get ('name')
            message = 'Hello {0}'.format (name)
            return Response ({'message' : message})
        else:
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get (self, request, format = None):
        """" Returns a list of features """""
        an_apiview = [ 'An API view uses HTTP methods as functions (get, post, patch, put, delete)',
        'It is similar to a traditional django view',
        'It gives control over the logic',
        'It maps manually to URLs']
        return Response ({'message' : 'Hello', 'an_apiview' : an_apiview})

    def put (self, request, pk = None):
        """" Handles updating an object """""
        return Response ({'method' : 'put'})

    def patch (self, request, pk = None):
        """" Updates the fields provided in the object """""
        return Response ({'method' : 'patch'})

    def delete (self, request, pk = None):
        """" Deletes the object """""
        return Response ({'method' : 'delete'})

class HelloViewSet (viewsets.ViewSet):
    """" Test API view set """""


    serializer_class = serializers.HelloSerializer


    def create (self, request):
        """" Create a new hello message """""
        serializer = serializers.HelloSerializer (data = request.data)
        if serializer.is_valid():
            name = serializer.data.get ('name')
            message = 'Hello {0}'.format (name)
            return Response ({'message' : message})
        else:
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve (self, request, pk = None):
        """" Reterieve a object by it's ID """""
        return Response ({'http_method' : 'GET'})

    def update (self, request, pk = None):
        """" Handles updating a object by it's ID """""
        return Response ({'http_method' : 'PUT'})

    def partial_update (self, request, pk = None):
        """" Handles updating part of a object by it's ID """""
        return Response ({'http_method' : 'PATCH'})

    def destory (self, request, pk = None):
        """" Handles removing an object by it's ID """""
        return Response ({'http_method' : 'Delete'})

    def list (self, request):
        """" Return a hello message """""

        a_viewset = [ 'Users actions (list, create, delete, update, partial_update)',
        'Automatically maps to URLS',
        'Provide more functionality with less code']

        return Response ({'message' : 'Hello!',
                        'a_viewset' : a_viewset})
