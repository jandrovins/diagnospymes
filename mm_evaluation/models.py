from django.db import models



VALID_SCORES = [
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
        ]

class Sector(models.Model):
    """The class Sector is for making a sectors table in MariaDB, based in economic secotrs in Colombia, the fields are: name is the sectors name in wich the company is involve, description is the description of the sector"""
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    class Meta():
        db_table = 'sector'


class PYME(models.Model):
    """the class PYME is for making a PYMES table in MariaDB, the filds are: sector_id refes to the id of sector the company is involve with, email_address refes to the username to login and the email of the company, pyme_name refers to the name of the company, password refers to an encrypted string, nit refers to a tributary number, phone_number refers to the company phone number, address is the companys address, contact_name is the name of the manager of the company, contact_number is the managers phone number, contact_sex is the sex of the maneger of the company, contact_birth_day is the managers birthday, contact_id_type is the managers id type, contact_id_number managers id number, contact_educational_level is the managers educational level, terms_conditions_acceptance a boolean true or false if the company accepts terms and contions, contact_time_on_charge is the managers time on charge of the company"""
    sector_id = models.ForeignKey(Sector, on_delete=models.CASCADE)
    email_address = models.CharField(max_length=100)
    pyme_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nit = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    contact_sex = models.CharField(max_length=10)
    contact_birth_day = models.DateTimeField()
    contact_id_type = models.CharField(max_length=30)
    contact_id_number = models.CharField(max_length=15)
    contact_education_level = models.CharField(max_length=40)
    terms_conditions_acceptance = models.BooleanField()
    contact_time_on_charge = models.IntegerField()

    class Meta:
        db_table = 'pyme'


class Autoevaluation(models.Model):
    """pyme_id is the id of the PYME for whom the autoevaluation will be filled out. 'start_time' refers to when the autoevaluation had begun. 'last_time_edition' refers to the last edition time of the autoevaluation. 'final_score' refers to the final ponderation, when all macroprocesses have been filled out."""
    pyme_id = models.ForeignKey(PYME, on_delete=models.CASCADE)
    start_time = models.DateField()
    last_time_edition = models.DateField()
    final_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_1_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_2_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_3_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_4_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_5_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_6_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_7_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_8_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_9_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_10_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)


    class Meta:
        db_table = 'autoevaluation'


"""This table contains the information regardin the different macroprocesses relevant to the self-evaluation process, which are 10 and describe the large areas of concern when it comes to logistical performance."""
class Macroprocess(models.Model):

    """Description is a text field which contains a brief explanations of a particular macroprocess."""
    description = models.CharField(max_length = 500, default="")
    """Name contains the macroprocess' high level name."""
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'macroprocess'


class Process(models.Model):
    """This is the database table where general information related to each process is stored. 'description' makes reference to the process sspecific description. Weight is needed when computing the macroprocess score. 'macroprocess_id' is the macroprocess to which the process belongs."""
    macroprocess_id = models.ForeignKey(Macroprocess, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500)
    guiding_question = models.CharField(max_length=400,default=' ')
    weight = models.FloatField()


    class Meta:
        db_table = 'process'


class Answer(models.Model):
    """When a process is evaluated in an autoevaluation an entry in the 'answer' table will be created."""
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE)
    autoevaluation_id = models.ForeignKey(Autoevaluation, on_delete=models.CASCADE)
    score = models.IntegerField(choices=VALID_SCORES)


    class Meta:
        db_table = 'answer'
        constraints = [
                models.UniqueConstraint(fields=['autoevaluation_id', 'process_id'], name='unique_answer'),
                ]


        """This table contains the information regarding specific practices, which are directly related to each level of each process and are used to describe the behaviour of a certain level in each process."""
class SpecificPractice(models.Model):
    """Process_id is a foreign key, which relates this specific practice to its corresponding process."""
    process_id = models.ForeignKey(Process,on_delete=models.CASCADE)
    """Score is the level of process this specific practive is related to, it is a number between 0 and 5."""
    score = models.IntegerField(choices=VALID_SCORES)
    """Description is a text field which contains a brief explanations of a particular specific practice."""
    description = models.CharField(max_length = 500)
    """Recommendation is a text which tells you how to achieve the level of this specific practice."""
    recommendation = models.CharField(max_length = 500)

    class Meta:
        db_table = 'specific_practice'


"""This table contains the information regarding general practices, which are related to global levels of performance and are used to describe briefly the behaviour of a PYME in a given level."""
class GeneralPractice(models.Model):
    """name refers to the name of the respective generl practice level"""
    name = models.CharField(max_length=40, default=' ')
    """Score is the level of overall logistic performance this specific practive is related to, it is a number between 0 and 5."""
    score = models.IntegerField(choices=VALID_SCORES)
    """Description is a text field which contains a brief explanations of a particular general practice."""
    description = models.CharField(max_length = 500)
    """Recommendation is a text which tells you how to achieve the level of this general practice."""
    recommendation = models.CharField(max_length = 500)

    class Meta:
        db_table = 'general_practice'


class Archive(models.Model):
    """The class Archive is for making an Archive table in MariaDB, the fields are: pyme_id refers to the autogenerated id of the pyme, file_object is a voluntary file that themanager can attach, file_type is the type of the file to be attach, file_name is the name of the file to attach"""
    pyme_id = models.ForeignKey(PYME,on_delete=models.CASCADE)
    file_object = models.FileField()
    file_type = models.CharField(max_length=10)
    file_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'archive'


class FinancesInformation(models.Model):
    """The class FinancesInformation is for making a finances information table in MariaDB, the filds are: pyme_id is the autogenerated id of a pyme, employees_number is the number of current imployees in the company, anual_income is the anual income of a company in Colombian pesos, assets are the assets of the company in Colombian pesos, liabilities are the liabilities of the company in Colombian pesos, monthly_production is the monthly production of the company in units or Colombian pesos, productive_configuration is the productive configuration of the company, inventory_politics are the inventory politics of the company, main_product is the main product the company sells, main_competidor is the main competidor of the company, patrimony is the patrimony of the company in Colombian pesos, sales_income is the sales income of the company in Colombian pesos, gross_profits are the gross profit of the company in Colombian pesos, net_profits are the net profits of the company in Colombian pesos, fixed_costs_expences are the fixed cost and expenses of the company, variable_costs_expences are the variable costs and expences of the company, ebitda is the EBITDA of the company"""
    pyme_id = models.ForeignKey(PYME,on_delete=models.CASCADE)
    employees_number = models.IntegerField()
    anual_income = models.BigIntegerField()
    assets = models.BigIntegerField()
    liabilities = models.IntegerField()
    monthly_production = models.BigIntegerField()
    productive_configuration = models.CharField(max_length=300)
    inventory_politics = models.CharField(max_length=100)
    main_product = models.CharField(max_length=30)
    main_competidor = models.CharField(max_length=30)
    patrimony = models.BigIntegerField()
    sales_income = models.BigIntegerField()
    gross_profits = models.BigIntegerField()
    net_profits = models.BigIntegerField()
    fixed_costs_expences = models.BigIntegerField()
    variable_costs_expences = models.BigIntegerField()
    ebitda = models.IntegerField()

    class Meta:
        db_table = 'finances_information'

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .general_use_functions import *
""" Function to update scores of the respective macroprocess in Autoevaluation instance each time an answer is created. When users is implemented, this should be used to get the actual current Autoevaluation instance. Macroprocesses IDs should range from 1 to 10"""
@receiver(post_save, sender=Answer)
def update_mps_on_autevaluation(sender, **kwargs):
    autoevaluation = get_autoevaluation(1)
    answer_list = Answer.objects.filter(autoevaluation_id=autoevaluation.id)

    # Actual scores of the MPs
    mps_scores = [0 for i in range(11)]
    # Percentages of the MPs that are alreay answered
    mps_percentages = [0 for i in range(11)]
    # Autoevaluation new total score
    total_score = 0

    for answer in answer_list:
        answers_process = Process.objects.get(pk=answer.process_id.id)
        mps_scores[answers_process.macroprocess_id.id] += answer.score * answers_process.weight
        mps_percentages[answers_process.macroprocess_id.id] += answers_process.weight
        print('JAJA')

    if mps_percentages[1] != 0:
        autoevaluation.macroprocess_1_score = mps_scores[1] * (1 / mps_percentages[1])
    if mps_percentages[2] != 0:
      autoevaluation.macroprocess_2_score = mps_scores[2] * (1 / mps_percentages[2])
    if mps_percentages[3] != 0:
      autoevaluation.macroprocess_3_score = mps_scores[3] * (1 / mps_percentages[3])
    if mps_percentages[4] != 0:
      autoevaluation.macroprocess_4_score = mps_scores[4] * (1 / mps_percentages[4])
    if mps_percentages[5] != 0:
      autoevaluation.macroprocess_5_score = mps_scores[5] * (1 / mps_percentages[5])
    if mps_percentages[6] != 0:
      autoevaluation.macroprocess_6_score = mps_scores[6] * (1 / mps_percentages[6])
    if mps_percentages[7] != 0:
      autoevaluation.macroprocess_7_score = mps_scores[7] * (1 / mps_percentages[7])
    if mps_percentages[8] != 0:
      autoevaluation.macroprocess_8_score = mps_scores[8] * (1 / mps_percentages[8])
    if mps_percentages[9] != 0:
      autoevaluation.macroprocess_9_score = mps_scores[9] * (1 / mps_percentages[9])
    if mps_percentages[10] != 0:
        autoevaluation.macroprocess_10_score = mps_scores[10] * (1 / mps_percentages[10])

    for score in mps_scores:
        total_score += score
    total_score /= 10


    autoevaluation.final_score = total_score
    autoevaluation.save()
    print("{} {} {}".format(total_score, autoevaluation.final_score, autoevaluation.macroprocess_1_score))

""" Function to delete entries of Answer, when a new Answer corresponding to the same process is created. When users is implemented, this should be used to get the actual current Autoevaluation instance. Macroprocesses IDs should range from 1 to 10"""
@receiver(pre_save, sender=Answer)
def update_answer(sender, instance, **kwargs):
    autoevaluation = get_autoevaluation(1)
    Answer.objects.filter(autoevaluation_id=autoevaluation.id, process_id=instance.process_id.id).delete()
