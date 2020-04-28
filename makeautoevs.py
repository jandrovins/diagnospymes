import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','diagnospymes.settings')
import django
django.setup()
from mm_evaluation.models import *
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

sect = Sector(name = 'Sector1', description = 'Sector de prueba')
sect.save()

for i in range(50):
    
    user = User.objects.create_user(randomString(), randomString(), 'password')
    user.save()

    p = PYME(user = user, contact_sex = 'fem', contact_phone_number = '123', contact_birth_date = timezone.now(), contact_id_type = 'CC', contact_id_number= '123', contact_time_on_charge = 5, contact_education_level = 'primaria', name = 'Jan', sector = sect, nit = 'nit', phone_number = '123', terms_conditions_acceptance = True)
    p.save()
    
    for j in range(2):

        mp1 = random.randint(0,5)
        mp2 = random.randint(0,5)
        mp3 = random.randint(0,5)
        mp4 = random.randint(0,5)
        mp5 = random.randint(0,5)
        mp6 = random.randint(0,5)
        mp7 = random.randint(0,5)
        mp8 = random.randint(0,5)
        mp9 = random.randint(0,5)
        mp10 = random.randint(0,5)
        avg = (mp1 + mp2 + mp3 + mp4 + mp5 + mp6 + mp7 + mp8 + mp9 + mp10)/10

        a = Autoevaluation(pyme = p, start_time = timezone.now(), last_time_edition = timezone.now(), final_score = avg, macroprocess_1_score = mp1, macroprocess_2_score = mp2, macroprocess_3_score = mp3, macroprocess_4_score = mp4, macroprocess_5_score = mp5, macroprocess_6_score = mp6, macroprocess_7_score = mp7,macroprocess_8_score = mp8, macroprocess_9_score = mp9, macroprocess_10_score = mp10)
        a.save()
        
