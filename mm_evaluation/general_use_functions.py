from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Answer, Autoevaluation, Process, PYME

def is_autoevaluation_filled(a):
    """Determines whether an autoevaluation is filled or not.
    
    Args:
        a (Autoevaluation): autoevaluation to make the test on.

    Returns:
        Boolean value. True if a is filled, false otherwise.
    
    """

    # If there are as many answers as there are processes, 'a' is completed.
    if len(Answer.objects.filter(autoevaluation=a.id)) == len(Process.objects.all()):
        return True
    return False

def get_autoevaluation(pyme):
    """Returns the last autoevaluation not completed for a given PYME, or a new one.

    Finds the first created Autoevaluation instance that has not been completed. If all are completed,
    it will create a new Autoevaluation instance to the PYME passed as argument, and return it.

    Args:
        pyme (PYME): model PYME instance.

    Returns:
        An Autoevaluation instance.

    """

    # PYME's object autoevaluations, ordered increasingly by start time
    autoevaluations_list = Autoevaluation.objects.filter(pyme=pyme).order_by('start_time')
    for autoevaluation in autoevaluations_list:
        if not is_autoevaluation_filled(autoevaluation):
            return autoevaluation
    # If all existing autoevaluations are completed, create a new one and return it
    return Autoevaluation(pyme=get_object_or_404(PYME, pk=pyme),
            start_time=timezone.now(),
            last_time_edition=timezone.now()
            )

def get_last_full_autoevaluation(pyme):
    """Returns the last full autoevaluation.

    This function returns the last created and completed Autoevaluation instance that belongs to the PYME instance passed as argument.

    Args:
        pyme (PYME): model PYME instance.

    Returns:
        None if there is no completed autoevaluation.

    """
    # PYME's object autoevaluations, order increasingly by start time
    autoevaluation_list = Autoevaluation.objects.filter(pyme=pyme).order_by('start_time')
    full_autoevaluation = None
    for autoevaluation in autoevaluation_list:
        if is_autoevaluation_filled(autoevaluation):
            full_autoevaluation = autoevaluation
    return full_autoevaluation


def get_lowest_macroprocess_number(macroprocesses_scores, lowest_score):
    """Returns a macroprocess number

    This function go over a dictionary of macroprocesses scores and found the value that matches the lowest score value in the dictionary

    Args:
        macroprocesses_scores: dictionary with macroprocesses numbers and scores (macroprocess_number, score)
        lowest_scores: the lowest score of macroprocess in the autoevaluation
    
    """
    for macroprocess_num, score in macroprocesses_scores.items(): 
        if lowest_score == score: 
            return macroprocess_num
