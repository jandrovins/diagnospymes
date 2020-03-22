from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .general_use_functions import *
from .models import Answer, Autoevaluation, Process, Macroprocess

import decimal



""" Function to update scores of the respective macroprocess in Autoevaluation instance each time an answer is created. When users is implemented, this should be used to get the actual current Autoevaluation instance."""
@receiver(post_save, sender=Answer)
def update_mps_on_autevaluation(sender, instance, **kwargs):
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

    if instance.process_id.macroprocess_id.id == 1:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_1_score / 10)
        autoevaluation.macroprocess_1_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_1_score / 10)
    if instance.process_id.macroprocess_id.id == 2:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_2_score / 10)
        autoevaluation.macroprocess_2_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_2_score / 10)
    if instance.process_id.macroprocess_id.id == 3:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_3_score / 10)
        autoevaluation.macroprocess_3_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_3_score / 10)
    if instance.process_id.macroprocess_id.id == 4:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_4_score / 10)
        autoevaluation.macroprocess_4_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_4_score / 10)
    if instance.process_id.macroprocess_id.id == 5:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_5_score / 10)
        autoevaluation.macroprocess_5_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_5_score / 10)
    if instance.process_id.macroprocess_id.id == 6:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_6_score / 10)
        autoevaluation.macroprocess_6_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_6_score / 10)
    if instance.process_id.macroprocess_id.id == 7:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_7_score / 10)
        autoevaluation.macroprocess_7_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_7_score / 10)
    if instance.process_id.macroprocess_id.id == 8:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_8_score / 10)
        autoevaluation.macroprocess_8_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_8_score / 10)
    if instance.process_id.macroprocess_id.id == 9:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_9_score / 10)
        autoevaluation.macroprocess_9_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_9_score / 10)
    if instance.process_id.macroprocess_id.id == 10:
        autoevaluation.final_score -= decimal.Decimal(autoevaluation.macroprocess_10_score / 10)
        autoevaluation.macroprocess_10_score = mps_score * (1 / mps_percentage)
        autoevaluation.final_score += decimal.Decimal(autoevaluation.macroprocess_10_score / 10)

    autoevaluation.save()

""" Function to delete entries of Answer, when a new Answer corresponding to the same process is created. When users is implemented, this should be used to get the actual current Autoevaluation instance. Macroprocesses IDs should range from 1 to 10"""
@receiver(pre_save, sender=Answer)
def update_answer(sender, instance, **kwargs):
    autoevaluation = Autoevaluation.objects.get(pk=instance.autoevaluation_id.id)
    Answer.objects.filter(autoevaluation_id=autoevaluation.id, process_id=instance.process_id.id).delete()
