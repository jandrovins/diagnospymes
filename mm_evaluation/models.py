from django.contrib.auth.models import User
from django.db import models


VALID_SCORES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        ]
"""Valid scores for answer instances."""

VALID_MACROPROCESS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        ]
"""Valid macroprocesses number."""

VALID_ID_TYPE = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ]
"""Valid ID type for PYME's contact."""

VALID_EDUCATION_LEVEL = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('tecnica', 'Técnica'),
        ('tecnologo', 'Tecnólogo'),
        ('universitario', 'Universitario'),
        ('posgrado', 'Posgrado'),
        ]
"""Valid education level for PYME's contact."""

VALID_ID_TYPE = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ]
"""Valid ID type for PYME's contact. """

VALID_EDUCATION_LEVEL = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('tecnica', 'Técnica'),
        ('tecnologo', 'Tecnólogo'),
        ('universitario', 'Universitario'),
        ('posgrado', 'Posgrado'),
        ]
"""Valid education level for PYME's contact. """

class Sector(models.Model):
    """Sector is the abstraction for economic sectors.

    Every PYME has to be related to a Sector.

    Fields:
        name (models.CharField): is the sector's name. Maximum is 20 characters.
        description (models.CharField): is the description of the sector. Maximum is 400 characters.
    """
    name        = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'sector'


class PYME(models.Model):
    """This model contains general information related to the company.

    Fields:
        user (models.OneToOneField): it is a Foreign key with auth.models.User. Used to manage authentication and accounting.
        contact_sex (models.CharField): is the sex of the company's contact. Maximum is 10 characters.
        contact_phone_number (models.CharField): is the company's contact phone number. Maximum is 10 characters.
        contact_birth_date (models.DateField): is the company's contact birthday.
        contact_id_type (models.CharField): is the company's contact id type. Maximum is 30 characters.
        contact_id_number (models.CharField): company's contact id number. Maximum is 15 characters.
        contact_time_on_charge (models.IntegerField): is the company's contact time on charge.
        contact_education_level (models.CharField): is the company's contact education level. Maximum is 40 characters.
        name (models.CharField): refers to the name of the company. Maximum is 100 characters.
        sector (models.ForeignKey): is a foreign key to Sector model.
        nit (models.CharField): refers to the tributary number of the company in Colombia. Maximum is 30 characters.
        address (models.CharField): is the company's general office address. Maximum is 50 characters.
        phone_number (models.CharField): refers to the company's phone number. Maximum is 10 characters.
        terms_conditions_acceptance (models.BooleanField): depends on whether the PYME has accepted our Terms and Conditions or not.

    """
    user                        = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_sex                 = models.CharField(max_length=10)
    contact_phone_number        = models.CharField(max_length=10)
    contact_birth_date          = models.DateField()
    contact_id_type             = models.CharField(max_length=30, choices=VALID_ID_TYPE)
    contact_id_number           = models.CharField(max_length=15)
    contact_time_on_charge      = models.IntegerField()
    contact_education_level     = models.CharField(max_length=40,choices=VALID_EDUCATION_LEVEL)
    name                        = models.CharField(max_length=100)
    sector                      = models.ForeignKey(Sector, on_delete=models.CASCADE)
    nit                         = models.CharField(max_length=30)
    address                     = models.CharField(max_length=50)
    phone_number                = models.CharField(max_length=10)
    terms_conditions_acceptance = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pyme'


class Autoevaluation(models.Model):
    """This model contains the summary result autoevaluations.

    This model is related to only one PYME object and as many Answer instances as the number of
    Process instances in existence.

    Fields:
        pyme (models.ForeignKey): PYME instance whom this autoevalution belongs.
        start_time (models.DateField): date when autoevaluation had begun.
        last_time_edition (models.DateField): autoevaluation's last edition date.
        final_score (models.DecimalField): refers to the final ponderation.
        macroprocess_*_score (models.DecimalField): is the mean score of the Answer instances (that have already
            been answered) whose Process instance belongs to this Macroprocess.

    """
    pyme                  = models.ForeignKey(PYME, on_delete=models.CASCADE)
    start_time            = models.DateField()
    last_time_edition     = models.DateField()
    final_score           = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_1_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_2_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_3_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_4_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_5_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_6_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_7_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_8_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_9_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_10_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return 'Autoevaluation of {} last edited on {}'.format(self.pyme.name, self.last_time_edition)

    class Meta:
        db_table = 'autoevaluation'


class Macroprocess(models.Model):
    """This model contains general information of each Macroprocess.

    This model contains the information regarding the different macroprocesses, which are 10 and describe the large 
    areas of concern when it comes to logistical performance.

    Fields:
        name (models.CharField): is the name of the macroprocess. Maximum is 50 characters.
        number (models.IntegerField): is the number identifying the macroprocess. ID is no sufficient
            because of the following scenario: if one deleted the the first macroprocess and created it again, 
            querying the macroprocess with ID 1 would fail, and instead one would have to query ID 11 (as we
            have always 10 macroprocesses). Having this field, one can query macroprocess with number 1, and
            it will always be the one we expect. Also, IDs depends on the order in which macroprocesses were added
            to the database. This field makes our lives easier.

    """

    name   = models.CharField(max_length = 50)
    number = models.IntegerField(choices=VALID_MACROPROCESS, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'macroprocess'
        ordering = ['number']


class Process(models.Model):
    """Saves each Process's information.

    This is the model where general information related to each process is stored. This will be used when creating
    Answer instances for autoevaluations.

    Fields:
        macroprocess (models.ForeignKey): is the macroprocess to which the process belongs.
        name (models.CharField): makes reference to the process's name. Maximum is 50 characters.
        description (models.CharField): makes reference to the process's description. Maximum is 500 characters.
        guiding_question (models.CharField): when answering the autoevaluation, this field will be used to help 
            the user this process's maturity level. Maximum is 400 characters.
        weight (models.FloatField): is needed when computing the macroprocess score.

    """
    macroprocess     = models.ForeignKey(Macroprocess, on_delete=models.CASCADE)
    name             = models.CharField(max_length=50, default='')
    description      = models.CharField(max_length=500)
    guiding_question = models.CharField(max_length=400,default=' ')
    weight           = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'process'


class Answer(models.Model):
    """Saves needed information to store the score related to a Process and an Autoevaluation
    
    When a process is evaluated in an autoevaluation, an instance of the Answer model will be created.

    Fields:
        process (models.ForeignKey): is the Process instance for whom this answer holds its score.
        autoevaluation (models.ForeignKey): is the Autoevaluation instance for whom this answer belongs.
        score (models.IntegerField): is the score given by the user.

    """
    process        = models.ForeignKey(Process, on_delete=models.CASCADE)
    autoevaluation = models.ForeignKey(Autoevaluation, on_delete=models.CASCADE)
    score          = models.IntegerField(choices=VALID_SCORES)

    def __str__(self):
        return 'Answer from {} to "{}" in autoevalution with id {}'.format(self.autoevaluation.pyme.name, self.process, self.autoevaluation.id)

    class Meta:
        db_table = 'answer'
        constraints = [
                models.UniqueConstraint(fields=['autoevaluation', 'process'], name='unique_answer'),
                ]


class SpecificPractice(models.Model):
    """Saves SpecificPractice instances related information.

    This table contains the information regarding specific practices, which are directly related to each level of 
    each process and are used to describe the behaviour of a certain level in each process.

    Fields:
        process (models.ForeignKey): is the process for whom this SpecificPractice instance belongs.
        score (models.IntegerField): Score is the level of process this specific practive is related to, 
            it is a number between 0 and 5.
        description (models.CharField): is a text field which contains a brief explanations of a particular
            specific practice. Maximum is 400 characters.
        recommendation (models.CharField): is a text which tells the user how to achieve the level of this 
            specific practice. Maximum is 400 characters.

    """
    process        = models.ForeignKey(Process,on_delete=models.CASCADE)
    score          = models.IntegerField(choices=VALID_SCORES)
    description    = models.CharField(max_length = 400)
    recommendation = models.CharField(max_length = 400)

    def __str__(self):
        return 'Specific practice for process {} on score {}'.format(self.process.name, self.process.score)

    class Meta:
        db_table = 'specific_practice'


class GeneralPractice(models.Model):
    """This model saves GeneralPractice instances information.

    This table contains the information regarding general practices, which are related to global levels of 
    performance and are used to describe briefly the behaviour of a PYME in a given level.
    
    Fields:
        name (models.CharField): refers to the name of the respective general practice level. Maximum is 40 characters.
        score (models.IntegerField): is the level of overall logistic performance this specific practive is related to,
            it is a number between 0 and 5.
        description (models.CharField): is a text field which contains a brief explanations of a particular general practice.
            Maximum is 500 characters.
        recommendation (models.CharField): is a text which tells you how to achieve the level of this general practice.
            Maximum is 500 characters.

    """
    name           = models.CharField(max_length=40, default='')
    score          = models.IntegerField(choices=VALID_SCORES)
    description    = models.CharField(max_length = 500)
    recommendation = models.CharField(max_length = 500)

    def __str__(self):
        return 'General practice {} to score {}'.format(self.name, self.score)

    class Meta:
        db_table = 'general_practice'


class Archive(models.Model):
    """This model saves important information for each file.

    The class Archive is for making an Archive table in MariaDB.

    Fields:
        pyme (models.ForeignKey): refers to the the pyme owner of this Archive instance.
        file_object (models.FileField): is a file that the manager can attach.
        file_type (models.CharField): is the type of the file attached. Maximum is 10 characters.
        name (models.CharField): is the name of the file attached. Maximum is 40 characters.

    """
    pyme        = models.ForeignKey(PYME,on_delete=models.CASCADE)
    file_object = models.FileField()
    file_type   = models.CharField(max_length=10)
    name        = models.CharField(max_length=40)

    def __str__(self):
        return 'File with name {} created by {}'.format(self.name, self.pyme.name)

    class Meta:
        db_table = 'archive'


class FinancesInformation(models.Model):
    """Saves finances information for each PYME registered.

    The class FinancesInformation is for making a finances information table in MariaDB. This hols general finances information
    for each PYME registered, and is mandatory that each PYME has at least one instance of this model.

    Fields:
        pyme (models.ForeignKey): is the PYME for whom this information belongs.
        employees_number (models.IntegerField): is the number of current employees in the company.
        anual_income (models.BigIntegerField): is the anual income of a company in Colombian pesos.
        assets (models.BigIntegerFields): are the assets of the company in Colombian pesos.
        liabilities (models.IntegerField): are the liabilities of the company in Colombian pesos.
        monthly_production (models.BigIntegerField): is the monthly production of the company in units or Colombian pesos.
        productive_configuration (models.CharField): is the productive configuration of the company. Maximum is 300 characters.
        inventory_politics (models.CharField): are the inventory politics of the company. Maximum is 100 characters.
        main_product (models.CharField): is the main product the company sells. Maximum is 30 characters.
        main_competidor (models.CharField): is the main competidor of the company. Maximum is 30 characters.
        patrimony (models.BigIntegerField): is the patrimony of the company in Colombian pesos.
        sales_income (models.BigIntegerField): is the sales income of the company in Colombian pesos.
        gross_profits (models.BigIntegerField): are the gross profit of the company in Colombian pesos.
        net_profits (models.BigIntegerField): are the net profits of the company in Colombian pesos.
        fixed_costs_expences (models.BigIntegerField): are the fixed cost and expenses of the company
        variable_costs_expences (models.BigIntegerField): are the variable costs and expences of the company.
        ebitda (models.IntegerField):is the EBITDA of the company

    """
    pyme                     = models.ForeignKey(PYME,on_delete=models.CASCADE)
    employees_number         = models.IntegerField()
    anual_income             = models.BigIntegerField()
    assets                   = models.BigIntegerField()
    liabilities              = models.IntegerField()
    monthly_production       = models.BigIntegerField()
    productive_configuration = models.CharField(max_length=300)
    inventory_politics       = models.CharField(max_length=100)
    main_product             = models.CharField(max_length=30)
    main_competidor          = models.CharField(max_length=30)
    patrimony                = models.BigIntegerField()
    sales_income             = models.BigIntegerField()
    gross_profits            = models.BigIntegerField()
    net_profits              = models.BigIntegerField()
    fixed_costs_expences     = models.BigIntegerField()
    variable_costs_expences  = models.BigIntegerField()
    ebitda                   = models.IntegerField()

    def __str__(self):
        return 'Finances information from {}'.format(self.pyme.name)

    class Meta:
        db_table = 'finances_information'
