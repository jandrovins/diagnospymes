from django.shortcuts import render
from django.http import HttpResponse

def autoevaluation(request):
    return HttpResponse("This is the autoevaluation")
