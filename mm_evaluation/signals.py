from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .general_use_functions import *
from .models import Answer, Autoevaluation, Process



""" Function to update scores of the respective macroprocess in Autoevaluation instance each time an answer is created. When users is implemented, this should be used to get the actual current Autoevaluation instance. Macroprocesses IDs should range from 1 to 10"""
@receiver(post_save, sender=Answer)
def update_mps_on_autevaluation(sender, instance, **kwargs):
    autoevaluation = Autoevaluation.objects.get(pk=instance.autoevaluation_id.id)
    answer_list = Answer.objects.filter(autoevaluation_id=autoevaluation.id)

    # Actual scores of the MPs
    mps_scores = [0 for i in range(11)]
    # Percentages of the MPs that are alreay answered
    mps_percentages = [0 for i in range(11)]
    # Autoevaluation new total score
    total_score = 0
    # Number of macroprocesses completed
    total_percentage = 0

    for answer in answer_list:
        answers_process = Process.objects.get(pk=answer.process_id.id)
        mps_scores[answers_process.macroprocess_id.id] += answer.score * answers_process.weight
        mps_percentages[answers_process.macroprocess_id.id] += answers_process.weight

    if mps_percentages[1] != 0:
        autoevaluation.macroprocess_1_score = mps_scores[1] * (1 / mps_percentages[1])
        total_percentage += 1
    if mps_percentages[2] != 0:
        autoevaluation.macroprocess_2_score = mps_scores[2] * (1 / mps_percentages[2])
        total_percentage += 1
    if mps_percentages[3] != 0:
        autoevaluation.macroprocess_3_score = mps_scores[3] * (1 / mps_percentages[3])
        total_percentage += 1
    if mps_percentages[4] != 0:
        autoevaluation.macroprocess_4_score = mps_scores[4] * (1 / mps_percentages[4])
        total_percentage += 1
    if mps_percentages[5] != 0:
        autoevaluation.macroprocess_5_score = mps_scores[5] * (1 / mps_percentages[5])
        total_percentage += 1
    if mps_percentages[6] != 0:
        autoevaluation.macroprocess_6_score = mps_scores[6] * (1 / mps_percentages[6])
        total_percentage += 1
    if mps_percentages[7] != 0:
        autoevaluation.macroprocess_7_score = mps_scores[7] * (1 / mps_percentages[7])
        total_percentage += 1
    if mps_percentages[8] != 0:
        autoevaluation.macroprocess_8_score = mps_scores[8] * (1 / mps_percentages[8])
        total_percentage += 1
    if mps_percentages[9] != 0:
        autoevaluation.macroprocess_9_score = mps_scores[9] * (1 / mps_percentages[9])
        total_percentage += 1
    if mps_percentages[10] != 0:
        autoevaluation.macroprocess_10_score = mps_scores[10] * (1 / mps_percentages[10])
        total_percentage += 1

    for score in mps_scores:
        total_score += score
    total_score /= total_percentage


    autoevaluation.final_score = total_score
    autoevaluation.save()

""" Function to delete entries of Answer, when a new Answer corresponding to the same process is created. When users is implemented, this should be used to get the actual current Autoevaluation instance. Macroprocesses IDs should range from 1 to 10"""
@receiver(pre_save, sender=Answer)
def update_answer(sender, instance, **kwargs):
    autoevaluation = Autoevaluation.objects.get(pk=instance.autoevaluation_id.id)
    Answer.objects.filter(autoevaluation_id=autoevaluation.id, process_id=instance.process_id.id).delete()
