from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError,transaction
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView, View
from django.views.generic.base import TemplateView

import plotly.graph_objs as go
import plotly.offline as opy

from .forms import  PYMERegistrationForm,UserRegistrationForm
from .general_use_functions import *
from .models import Answer, Autoevaluation, Macroprocess, Process,  PYME




@login_required
def begin_or_continue_autoevaluation(request):
    autoevaluation = get_autoevaluation(request.user.pyme.pk)
    autoevaluation.save()
    return HttpResponseRedirect(
            reverse('mm_evaluation:autoevaluation', args=(autoevaluation.id,))
            )

class AutoevaluationView(LoginRequiredMixin, ListView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para responder las autoevaluaciones."

    # For use in ListView
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autoevaluation'] = self.autoevaluation
        if is_autoevaluation_filled(self.autoevaluation):
            context['is_autoevaluation_filled'] = True
        return context

    def get(self, request, pk, *args, **kwargs):
        self.autoevaluation = get_object_or_404(Autoevaluation, pk=pk)
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

    def post(self, request,  autoevaluation_id):
        autoevaluation = get_object_or_404(Autoevaluation, pk=autoevaluation_id)
        
        for key, value in request.POST.items():
            if 'score_' in key:
                score = value
                if score != '':
                    answer = Answer(autoevaluation_id=autoevaluation, process_id=Process.objects.get(id=int(key.split('_')[1])), score=score)
                    answer.save()
        
        return HttpResponseRedirect(reverse_lazy('mm_evaluation:autoevaluation', args=(autoevaluation.id,))+'?page='+str(answer.process_id.macroprocess_id.number))




class ProcessAlreadyAnswerView(LoginRequiredMixin, TemplateView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    template_name = 'mm_evaluation/process_already_answer.html'



class IndexView(View):
    template_name = 'mm_evaluation/index.html'
    context_object_name = 'general_list'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

class Mission(View):
    template_name = 'mm_evaluation/mission.html'
    context_object_name = 'general_list'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

class AboutUs(View):
    template_name = 'mm_evaluation/index.html'
    context_object_name = 'general_list'
    
    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

class Vision(View):
    template_name = 'mm_evaluation/vision.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

class Metodology(View):
    template_name = 'mm_evaluation/metodology.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))
    
class Requirements(View):
    template_name = 'mm_evaluation/requirements.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

class Instructions(View):
    template_name = 'mm_evaluation/instructions.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

    
class PreviousResults(LoginRequiredMixin, ListView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    template_name = 'mm_evaluation/previousresults.html'
    context_object_name = 'all_previous_results'

    def get_queryset(self):
        return Autoevaluation.objects.filter(pyme_id_id=1,final_score__isnull=False).order_by('last_time_edition')

      
class ResultDetail(LoginRequiredMixin, DetailView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    model = Autoevaluation
    template_name = 'mm_evaluation/resultdetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_autoev = super().get_object()
     
        x = ['MP1', 'MP2', 'MP3', 'MP4', 'MP5', 'MP6', 'MP7', 'MP8', 'MP9', 'MP10']
        y = []

        y.append(current_autoev.macroprocess_1_score)
        y.append(current_autoev.macroprocess_2_score)
        y.append(current_autoev.macroprocess_3_score)
        y.append(current_autoev.macroprocess_4_score)
        y.append(current_autoev.macroprocess_4_score)
        y.append(current_autoev.macroprocess_5_score)
        y.append(current_autoev.macroprocess_6_score)
        y.append(current_autoev.macroprocess_7_score)
        y.append(current_autoev.macroprocess_8_score)
        y.append(current_autoev.macroprocess_9_score)
        y.append(current_autoev.macroprocess_10_score)
        
        data = [go.Bar(x=x, y=y)]
        layout=go.Layout(title="Puntaje", xaxis={'title':'Macroproceso'}, yaxis={'title':'Resultado'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div

        return context

class Resources(View):
    template_name = 'mm_evaluation/resources.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))


class SuccessfulRegistrationView(LoginRequiredMixin, TemplateView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    template_name = "mm_evaluation/successful_registration.html"

@transaction.atomic
def registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': # when user sends registration info:
        user_form = UserRegistrationForm(request.POST, prefix="user")
        PYME_form = PYMERegistrationForm(request.POST, prefix="PYME")
        if PYME_form.is_valid() and user_form.is_valid():
            user = user_form.save()

            user.refresh_from_db()  # This will load the PYME created by the Signal
            PYME_form.full_clean() # Manually clean the form this time
            PYME = PYME_form.save(commit=False)
            PYME.user = user

            PYME_form.save()  # Gracefully save the form

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('mm_evaluation:successful_registration'))

    # if a GET (or any other method) we'll create a blank form
    else:
        user_registration_form = UserRegistrationForm(prefix="user")
        PYME_registration_form = PYMERegistrationForm(prefix="PYME")

    return render(request, 'mm_evaluation/registration.html', {
        'user_registration_form': user_registration_form,
        'PYME_registration_form': PYME_registration_form,
        })
