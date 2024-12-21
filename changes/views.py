from django.shortcuts import render
from django.http import HttpResponse

def changes_1(request):
    return HttpResponse('Changes')
