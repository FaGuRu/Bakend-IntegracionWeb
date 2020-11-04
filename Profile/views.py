from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
import json
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions

# --------------MODELOS-------------------
from Profile.models import ProfileModel
from Profile.models import Users

# -----------SERIALIZERS--------------------
from Profile.serializers import ProfileModelSerializers
from Profile.serializers import UserSerializer
from django.contrib import messages

# -------------------VIEWS-----------------##
# class ProfileModelView(APIView):
#         queryset=models.Users.objects.all()
#         serializer_class=serializers.ProfileModelSerializers

#         def post(self, request, format=None):
#             serializer = ProfileModelSerializers(data = request.data, context = {'request': request}) # Va a invocar a una clase de serializador
#             if(serializer.is_valid()):
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response("Error Formato")

#----------------------View tabla-----------------------#
class UsersViewset(APIView):
        def get(self,request,format=None):
            users = Users.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)


        def post(self, request, format=None):
            serializer = UserSerializer(data = request.data, context = {'request': request}) # Va a invocar a una clase de serializador
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response("Error Formato")

        def delete(self,request,pk,format=None):
            task = UserSerializer.objects.get(id=pk)
            task.delete()

        def put(self,request,pk):
            task = UserSerializer.objects.get(id=pk)
            serializer = UserSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)
