from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
