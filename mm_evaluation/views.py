from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db import IntegrityError

from .models import Process, Macroprocess, Autoevaluation, Answer
from .forms import PunctuateProcessForm

class AutoevaluationView(ListView):
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

class ProcessAlreadyAnswerView(TemplateView):
    template_name = 'mm_evaluation/process_already_answer.html'

def save_answer(request, pk):
    autoevaluation = get_object_or_404(Autoevaluation, pk=1)
    process = get_object_or_404(Process, pk=pk)
    try:
        answer = Answer(autoevaluation_id=autoevaluation, process_id=process, score=request.POST['score'])
        answer.save()
    except (IntegrityError):
        return HttpResponseRedirect(reverse('mm_evaluation:process_already_answer'))
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mm_evaluation:autoevaluation'))
