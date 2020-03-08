

from django.shortcuts import render
from .models import Macroprocess, SpecificPractice, GeneralPrcatice 
# Create your views here.

def SpecificPracticeView(generic.SpecificPracticeView):

def general(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def MacroprocessView(generic.MacroprocessView):
    

