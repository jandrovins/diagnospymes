from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Autoevaluation, PYME, Answer, Process

def is_autoevaluation_filled(a):
    # If there are as many answers as there are processes, 'a' is completed.
    if len(Answer.objects.filter(autoevaluation_id=a.id)) == len(Process.objects.all()):
        return True
    return False

""" This function returns the first created Autoevaluation that has not been completed. If all are completed, it will return a new instance of the autoevaluation."""
def get_autoevaluation(pyme_id):
    autoevaluations_list = Autoevaluation.objects.filter(pyme_id=pyme_id).order_by('start_time')
    for autoevaluation in autoevaluations_list:
        if not is_autoevaluation_filled(autoevaluation):
            return autoevaluation

    return Autoevaluation(pyme_id=get_object_or_404(PYME, pk=pyme_id),
            start_time=timezone.now(),
            last_time_edition=timezone.now()
            )

def get_last_full_autoevaluation(pyme_id):
    autoevaluation_list = Autoevaluation.objects.filter(pyme_id=pyme_id).order_by('start_time')
    for autoevaluation in autoevaluation_list:
        if is_autoevaluation_filled(autoevaluation):
            full_autoevaluation = autoevaluation
    return full_autoevaluation

