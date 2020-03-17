from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Autoevaluation, PYME, Answer, Process

def is_autoevaluation_filled(a):
    # If there are as many answers as there are processes, 'a' is completed.
    if len(Answer.objects.filter(autoevaluation_id=a.id)) == len(Process.objects.all()):
        return True
    return False

def get_autoevaluation(pyme_id):
    # When login is working, this should be edited accordingly. pyme_id in the filter query is the id of the pyme that is filling que autoevaluation.
    autoevaluations_list = Autoevaluation.objects.filter(pyme_id=pyme_id).order_by('start_time')
    for autoevaluation in autoevaluations_list:
        if not is_autoevaluation_filled(autoevaluation):
            return autoevaluation

    return Autoevaluation(pyme_id=get_object_or_404(PYME, pk=1),
            start_time=timezone.now(),
            last_time_edition=timezone.now()
            )
