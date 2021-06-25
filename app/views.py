from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_spectacular.types import OpenApiTypes


@extend_schema(
        examples=[
                    OpenApiExample(
                        name='health',
                        value='{ \"status\": \"UP\" }'
                    ),
                ],
        description='Health response',
        responses=OpenApiTypes.OBJECT, 
     ) 
@api_view(['GET'])
def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def index(request):
    return render(request, 'index.html')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
