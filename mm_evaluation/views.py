from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
from plotly.subplots import make_subplots

from .forms import  PYMERegistrationForm,UserRegistrationForm
from .general_use_functions import *
from .models import Answer, Autoevaluation, Macroprocess, Process,  PYME

@login_required
def begin_or_continue_autoevaluation(request):
    """This view reddirects to the autoevaluation that should be filled.

    This view should allways be accessed before AutoevaluationView, as this view will
    pass the Autoevaluation instance ID as argument. The objective of this view is to
    find the first created but not completed autoevaluation belonging to the PYME logged in,
    and redirect to mm_evaluation:autoevaluation passing the autoevaluation ID as argument.
    If there are no completed autoevaluations, this view will create one, and pass it instead.

    Args:
        request (HttpRequest): HttpRequest object holding state and metadata for the request made.

    Returns:
        HttpResponseReddirect object pointing to AutoevaluationView and passing the ID of the
        autoevaluation's to be scored as argument.

    """

    autoevaluation = get_autoevaluation(request.user.pyme.pk)
    autoevaluation.save()
    return HttpResponseRedirect(
            reverse('mm_evaluation:autoevaluation', args=(autoevaluation.id,))
            )

class AutoevaluationView(LoginRequiredMixin, ListView):
    """View to handle Autoevaluation instances scoring.

    Inherits from LoginRequiredMixin and ListView. Shows processes separated on macroprocesses,
    and uses pagination for macroprocesses. This is, for each page, one macroprocess and its processes
    will be displayed. Also, a form to score each process will be rendered.

    """
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para responder las autoevaluaciones."

    # For use in ListView
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

    def test_user_owns_autoevaluation(self, user, autoevaluation):
        """ Method to test if user owns the autoevaluation that is accessing.

        Args:
            user (User): the User object that is accessing the autoealuations page.
            autoevaluation (Autoevaluation): the autoevaluation that the user is trying
                to access.

        Returns:
            A boolean, indicating whether the user.pyme object equals autoevaluation.pyme.

        """
        return user.pyme == autoevaluation.pyme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autoevaluation'] = self.autoevaluation
        return context

    def get(self, request, pk, *args, **kwargs):
        self.autoevaluation = get_object_or_404(Autoevaluation, pk=pk)
        # Check if user owns autoevaluation
        if not self.test_user_owns_autoevaluation(request.user, self.autoevaluation):
            return redirect(reverse('mm_evaluation:denied_access'))
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

    def post(self, request, process_id, autoevaluation_id):
        autoevaluation = get_object_or_404(Autoevaluation, pk=autoevaluation_id)
        # Check if user owns autoevaluation
        if not self.test_user_owns_autoevaluation(request.user, autoevaluation):
            return redirect(reverse('mm_evaluation:denied_access'))
        process = get_object_or_404(Process, pk=process_id)
        answer = Answer(autoevaluation=autoevaluation, process=process, score=request.POST['score'])
        autoevaluation.last_time_edition = timezone.now()
        autoevaluation.save()
        answer.save()
        return HttpResponseRedirect(reverse_lazy('mm_evaluation:autoevaluation', args=(autoevaluation.id,)))

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
    template_name = 'mm_evaluation/methodology.html'

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
        self.pyme = get_object_or_404(PYME, user=self.request.user)
        return Autoevaluation.objects.filter(pyme=self.pyme).order_by('last_time_edition')

    
class ResultDetail(LoginRequiredMixin, DetailView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    model = Autoevaluation
    template_name = 'mm_evaluation/resultdetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.autoevaluation = super().get_object()
     
        x = ['MP1', 'MP2', 'MP3', 'MP4', 'MP5', 'MP6', 'MP7', 'MP8', 'MP9', 'MP10']
        y = []

        y.append(self.autoevaluation.macroprocess_1_score)
        y.append(self.autoevaluation.macroprocess_2_score)
        y.append(self.autoevaluation.macroprocess_3_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_5_score)
        y.append(self.autoevaluation.macroprocess_6_score)
        y.append(self.autoevaluation.macroprocess_7_score)
        y.append(self.autoevaluation.macroprocess_8_score)
        y.append(self.autoevaluation.macroprocess_9_score)
        y.append(self.autoevaluation.macroprocess_10_score)
        
        data = [go.Bar(x=x, y=y)]
        layout=go.Layout(title="Puntaje", xaxis={'title':'Macroproceso'}, yaxis={'title':'Resultado'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div

        return context

    def get(self, request, *args, **kwargs):
        response_class = super().get(request, *args, **kwargs)
        if not request.user.pyme == self.autoevaluation.pyme:
            return redirect(reverse('mm_evaluation:denied_access'))
        return response_class

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
    """This view handles registration page.

    Creates two forms: UserRegistrationForm and PYMERegistrationForm. The former is used 
    to get information related to the User model and the latter information related to the PYME
    model.

    Args:
        request (HttpRequest): HttpRequest object holding state and metadata for the request made.

    Returns:
        HttpResponse redirecting to home page if registration succeded. If some form fields are
        invalid, displays the errors and redirects to registration page.

    """
    user_form = UserRegistrationForm(request.POST, prefix="user")
    PYME_form = PYMERegistrationForm(request.POST, prefix="PYME")
    # if this is a POST request we need to process the form data
    if request.method == 'POST': # when user sends registration info:

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

        user_form = UserRegistrationForm(prefix="user")
        PYME_form = PYMERegistrationForm(prefix="PYME")

    return render(request, 'mm_evaluation/registration.html', {
        'user_registration_form': user_form,
        'PYME_registration_form': PYME_form,
        })

class AccessDeniedView(TemplateView):
    """View used when a user is accessing a page that does not belong to him.
    Renders a template that displays an error message and a link to home page.
    This view should be redirected to whenever a user is trying to access model instances
    that are not linkes to its PYME object (i.e. user.pyme).
    """
    template_name = "mm_evaluation/denied_access.html"

class Benchmarking(LoginRequiredMixin, ListView):
    # For use in LoginRequiredMixin
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    template_name = 'mm_evaluation/benchmarking.html'
    context_object_name = 'all_previous_results'

    def get_queryset(self):
        self.pyme = get_object_or_404(PYME, user=self.request.user)
        return Autoevaluation.objects.filter(pyme=self.pyme).order_by('last_time_edition')

    
class BenchmarkingTop(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    model = Autoevaluation
    template_name = 'mm_evaluation/benchmarkingTop.html'

    def get_context_data(self, **kwargs):
        """Top autoevaluations query"""
        top = round(Autoevaluation.objects.all().count() * 0.05) #Finds how many autoevaluations are 5% of the autoevaluations
        q = Autoevaluation.objects.order_by('-final_score')[0:top] #Finds the top 5% of the autoevaluations

        #Initialices all the aux_variables that will hold the average value of the top 5% of autoevaluations to 0
        mp1 = 0
        mp2 = 0
        mp3 = 0
        mp4 = 0
        mp5 = 0
        mp6 = 0
        mp7 = 0
        mp8 = 0
        mp9 = 0
        mp10 = 0
        total = 0

        for a in q:
            mp1 += (a.macroprocess_1_score / top)
            mp2 += (a.macroprocess_2_score / top)
            mp3 += (a.macroprocess_3_score / top)
            mp4 += (a.macroprocess_4_score / top)
            mp5 += (a.macroprocess_5_score / top)
            mp6 += (a.macroprocess_6_score / top)
            mp7 += (a.macroprocess_7_score / top)
            mp8 += (a.macroprocess_8_score / top)
            mp9 += (a.macroprocess_9_score / top)
            mp10 += (a.macroprocess_10_score / top)
            total += (a.final_score / top)
            
        avg = [mp1, mp2, mp3, mp4, mp5, mp6, mp7, mp8, mp9, mp10]

        context = super().get_context_data(**kwargs)

        self.autoevaluation = super().get_object()

        x = ['MP1', 'MP2', 'MP3', 'MP4', 'MP5', 'MP6', 'MP7', 'MP8', 'MP9', 'MP10']
        y = []

        y.append(self.autoevaluation.macroprocess_1_score)
        y.append(self.autoevaluation.macroprocess_2_score)
        y.append(self.autoevaluation.macroprocess_3_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_5_score)
        y.append(self.autoevaluation.macroprocess_6_score)
        y.append(self.autoevaluation.macroprocess_7_score)
        y.append(self.autoevaluation.macroprocess_8_score)
        y.append(self.autoevaluation.macroprocess_9_score)
        y.append(self.autoevaluation.macroprocess_10_score)

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=x, y=y, name="Mis Resultados"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=x, y=avg, name="Los mejores resultados"),
            secondary_y=True,
        )

        fig.update_layout(
            title_text="Comparar con el mejor"
        )

        fig.update_xaxes(title_text="Nombre macroproceso")

        fig.update_yaxes(title_text="Benchmarking",range=[0, 5.5], secondary_y=False)
        fig.update_yaxes(title_text="Comparacion con el mejor", range=[0, 5.5], secondary_y=True)
        
        div = opy.plot(fig, auto_open=False, output_type='div')

        context = {'graph' : div,
                   'text' : 'Comparar con el mejor',
	           'total' : total,
                   'mine' : self.autoevaluation.final_score,
                   'type' : 'mejor'
                    }

        return context

class BenchmarkingBottom(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    model = Autoevaluation
    template_name = 'mm_evaluation/benchmarkingTop.html'

    def get_context_data(self, **kwargs):
        """Top autoevaluations query"""
        top = round(Autoevaluation.objects.all().count() * 0.05) #Finds how many autoevaluations are 5% of the autoevaluations
        q = Autoevaluation.objects.order_by('final_score')[0:top] #Finds the top 5% of the autoevaluations

        #Initialices all the aux_variables that will hold the average value of the top 5% of autoevaluations to 0
        mp1 = 0
        mp2 = 0
        mp3 = 0
        mp4 = 0
        mp5 = 0
        mp6 = 0
        mp7 = 0
        mp8 = 0
        mp9 = 0
        mp10 = 0
        total = 0

        for a in q:
            mp1 += (a.macroprocess_1_score / top)
            mp2 += (a.macroprocess_2_score / top)
            mp3 += (a.macroprocess_3_score / top)
            mp4 += (a.macroprocess_4_score / top)
            mp5 += (a.macroprocess_5_score / top)
            mp6 += (a.macroprocess_6_score / top)
            mp7 += (a.macroprocess_7_score / top)
            mp8 += (a.macroprocess_8_score / top)
            mp9 += (a.macroprocess_9_score / top)
            mp10 += (a.macroprocess_10_score / top)
            total += (a.final_score / top)
            
        avg = [mp1, mp2, mp3, mp4, mp5, mp6, mp7, mp8, mp9, mp10]

        context = super().get_context_data(**kwargs)

        self.autoevaluation = super().get_object()

        x = ['MP1', 'MP2', 'MP3', 'MP4', 'MP5', 'MP6', 'MP7', 'MP8', 'MP9', 'MP10']
        y = []

        y.append(self.autoevaluation.macroprocess_1_score)
        y.append(self.autoevaluation.macroprocess_2_score)
        y.append(self.autoevaluation.macroprocess_3_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_5_score)
        y.append(self.autoevaluation.macroprocess_6_score)
        y.append(self.autoevaluation.macroprocess_7_score)
        y.append(self.autoevaluation.macroprocess_8_score)
        y.append(self.autoevaluation.macroprocess_9_score)
        y.append(self.autoevaluation.macroprocess_10_score)

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=x, y=y, name="Mis Resultados"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=x, y=avg, name="Los peores resultados"),
            secondary_y=True,
        )

        fig.update_layout(
            title_text="Comparar con el peor"
        )

        fig.update_xaxes(title_text="Nombre macroproceso")

        fig.update_yaxes(title_text="Benchmarking",range=[0, 5.5], secondary_y=False)
        fig.update_yaxes(title_text="Comparacion con el peor", range=[0, 5.5], secondary_y=True)
        
        div = opy.plot(fig, auto_open=False, output_type='div')

        context = {'graph' : div,
                   'text' : 'Comparar con el peor',
	           'total' : total,
                   'mine' : self.autoevaluation.final_score,
                   'type' : 'peor'
                    }

        return context

class BenchmarkingAverage(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('mm_evaluation:login')
    permission_denied_message = "Debes ingresar a tu cuenta para acceder a esta sección."

    model = Autoevaluation
    template_name = 'mm_evaluation/benchmarkingTop.html'

    def get_context_data(self, **kwargs):
        """Top autoevaluations query"""
        top = round(Autoevaluation.objects.all().count() * 0.5) #Finds how many autoevaluations are 5% of the autoevaluations
        q = Autoevaluation.objects.order_by('final_score')[top] #Finds the bottom 5% of the autoevaluations

        avg = [q.macroprocess_1_score, q.macroprocess_2_score, q.macroprocess_3_score, q.macroprocess_4_score, q.macroprocess_5_score, q.macroprocess_6_score, q.macroprocess_7_score, q.macroprocess_8_score, q.macroprocess_9_score, q.macroprocess_10_score]
            

        context = super().get_context_data(**kwargs)

        self.autoevaluation = super().get_object()

        x = ['MP1', 'MP2', 'MP3', 'MP4', 'MP5', 'MP6', 'MP7', 'MP8', 'MP9', 'MP10']
        y = []

        y.append(self.autoevaluation.macroprocess_1_score)
        y.append(self.autoevaluation.macroprocess_2_score)
        y.append(self.autoevaluation.macroprocess_3_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_4_score)
        y.append(self.autoevaluation.macroprocess_5_score)
        y.append(self.autoevaluation.macroprocess_6_score)
        y.append(self.autoevaluation.macroprocess_7_score)
        y.append(self.autoevaluation.macroprocess_8_score)
        y.append(self.autoevaluation.macroprocess_9_score)
        y.append(self.autoevaluation.macroprocess_10_score)

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=x, y=y, name="Mis Resultados"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=x, y=avg, name="Los resultados promedio"),
            secondary_y=True,
        )

        fig.update_layout(
            title_text="Comparar con el promedio"
        )

        fig.update_xaxes(title_text="Nombre macroproceso")

        fig.update_yaxes(title_text="Benchmarking",range=[0, 5.5], secondary_y=False)
        fig.update_yaxes(title_text="Comparacion con el promedio", range=[0, 5.5], secondary_y=True)
        
        div = opy.plot(fig, auto_open=False, output_type='div')

        context = {'graph' : div,
                   'text' : 'Comparar con el promedio',
                   'total' : q.final_score,
                   'mine' : self.autoevaluation.final_score,
                   'type' : 'promedio'
                    }

        return context

