import decimal
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .general_use_functions import *
from .models import Answer, Autoevaluation, Process, Macroprocess



@receiver(post_save, sender=Answer)
def update_mps_on_autevaluation(sender, instance, **kwargs):
    """When a Answer is created by the user, this signal recalculates its Autoevaluation instance's macroprocess score.

    Signal to update score of its respective macroprocess in Autoevaluation instance each time an answer is created.

    Args:
        sender (Model): model which activates this signal.
        instance (Answer): instance whose save method activated this signal. Its model attributes may be accessed.
        **kwargs (dictionary): other parameters.

    Returns:
        Nothing.

    """
    # The autoevaluation to which 'instance' belongs
    autoevaluation = Autoevaluation.objects.get(id=instance.autoevaluation_id.id)
    # The list of answers belonging to a Process that belongs to the same Macroprocess as 'instance' that have been answered in the current autevaluation.
    answer_list = Answer.objects.filter(autoevaluation_id=autoevaluation, process_id__macroprocess_id=instance.process_id.macroprocess_id)

    # Actual scores of the MPs
    mps_score = 0
    # Percentages of the MPs that are alreay answered
    mps_percentage = 0

    for answer in answer_list:
        answers_process  = Process.objects.get(id=answer.process_id.id)
        mps_score += answer.score * answers_process.weight
        mps_percentage += answers_process.weight

    if instance.process_id.macroprocess_id.number == 1:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_1_score / 10)
        autoevaluation.macroprocess_1_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_1_score / 10)
    if instance.process_id.macroprocess_id.number == 2:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_2_score / 10)
        autoevaluation.macroprocess_2_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_2_score / 10)
    if instance.process_id.macroprocess_id.number == 3:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_3_score / 10)
        autoevaluation.macroprocess_3_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_3_score / 10)
    if instance.process_id.macroprocess_id.number == 4:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_4_score / 10)
        autoevaluation.macroprocess_4_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_4_score / 10)
    if instance.process_id.macroprocess_id.number == 5:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_5_score / 10)
        autoevaluation.macroprocess_5_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_5_score / 10)
    if instance.process_id.macroprocess_id.number == 6:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_6_score / 10)
        autoevaluation.macroprocess_6_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_6_score / 10)
    if instance.process_id.macroprocess_id.number == 7:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_7_score / 10)
        autoevaluation.macroprocess_7_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_7_score / 10)
    if instance.process_id.macroprocess_id.number == 8:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_8_score / 10)
        autoevaluation.macroprocess_8_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_8_score / 10)
    if instance.process_id.macroprocess_id.number == 9:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_9_score / 10)
        autoevaluation.macroprocess_9_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_9_score / 10)
    if instance.process_id.macroprocess_id.number == 10:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_10_score / 10)
        autoevaluation.macroprocess_10_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_10_score / 10)

    autoevaluation.save()

@receiver(pre_save, sender=Answer)
def update_answer(sender, instance, **kwargs):
    """Updates a Answer instance with a new score.

    When the user creates an Answer instance to a Process instance that had already an Answer instance in the
    user's current Autoevaluation instance, this signal deletes previous answer, so each process only has one
    instance of Answer per autoevaluation.

    Args:
        sender (Model): model which activates this signal.
        instance (Answer): instance whose save method activated this signal. Its model attributes may be accessed.
        kwargs (dictionary): other attributes may be passed.

    Returns:
        Nothing.

    """
    autoevaluation = Autoevaluation.objects.get(pk=instance.autoevaluation_id.id)
    Answer.objects.filter(autoevaluation_id=autoevaluation.id, process_id=instance.process_id.id).delete()

@receiver(post_save, sender=Answer)
def update_autoevaluation_last_edition(sender, instance, **kwargs):
    """Updates the last_edition field in Answer instance's autoevaluation.

    Signal to update last_time_edition filed in Autoevaluation instance when an Answer is created. I.e. when the autoevaluation is edited.

    Attributes:
        sender (Model): model whose save() method activates this signal.
        instance (Answer): instance whose save method activated this signal. Its model attributes may be accessed.
        kwargs (dictionary): other attributes may be passed.

    Returns:
        Nothing.

    """
    autoevaluation = Autoevaluation.objects.get(pk=instance.autoevaluation_id.id)
    autoevaluation.last_time_edition = timezone.now()
    autoevaluation.save()
