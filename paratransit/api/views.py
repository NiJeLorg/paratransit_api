# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# import all api models
from api.models import *

# Api views here.
def api_index(request):
	response = {'foo': 'bar'}
	return JsonResponse(response)
