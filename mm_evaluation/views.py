from django.db import IntegrityError
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Process, Macroprocess, Autoevaluation, Answer, PYME
from .forms import PunctuateProcessForm

class AutoevaluationView(ListView):
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

    def is_autoevaluation_filled(self, a):
        if a.final_score == None:
            return False
        return True

    def get_autoevaluation(self):
        # When login is working, this should be edited accordingly. pyme_id in the filter query is the id of the pyme that is filling que autoevaluation.
        autoevaluations_list = Autoevaluation.objects.filter(pyme_id=1).order_by('start_time')
        for autoevaluation in autoevaluations_list:
            if not self.is_autoevaluation_filled(autoevaluation):
                return autoevaluation

        return Autoevaluation(pyme_id=1,
                start_time=timezone.now(),
                last_time_edition=timezone.now()
                )


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, pk):
        autoevaluation = self.get_autoevaluation()
        process = get_object_or_404(Process, pk=pk)
        try:
            answer = Answer(autoevaluation_id=autoevaluation, process_id=process, score=request.POST['score'])
            autoevaluation.last_time_edition = timezone.now()
            answer.save()
        except (IntegrityError):
            return HttpResponseRedirect(reverse('mm_evaluation:process_already_answer'))
        else:
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('mm_evaluation:autoevaluation'))


class ProcessAlreadyAnswerView(TemplateView):
    template_name = 'mm_evaluation/process_already_answer.html'
