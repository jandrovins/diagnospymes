from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Process, Macroprocess

class Autoevaluation(ListView):
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

    #def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get a context
    #    context = super().get_context_data(**kwargs)
    #    # Add in a QuerySet of all the books
    #    context['process_list'] = Process.objects.all()
    #    return context
