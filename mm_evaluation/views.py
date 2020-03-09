from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Process, Macroprocess, Autoevaluation

class Autoevaluation(ListView):
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

def view_results(request, autoevaluation_id):
    autoevaluation = get_object_or_404(Autoevaluation, pk=autoevaluation_id)
:   try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

