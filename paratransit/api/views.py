# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# import all api models
from api.models import *

#for django rest framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *

# Api views here.
def api_index(request):
	response = {'foo': 'bar'}
	return JsonResponse(response)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TripsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trips to be viewed or edited.
    """
    queryset = trips.objects.all()
    serializer_class = TripsSerializer