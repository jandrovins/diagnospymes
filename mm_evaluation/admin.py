from django.contrib import admin

from .models import Sector, PYME, Autoevaluation, Macroprocess, Process, Answer, SpecificPractice, GeneralPractice, Archive, FinancesInformation

admin.site.register(Macroprocess)
admin.site.register(Process)
admin.site.register(SpecificPractice)
admin.site.register(GeneralPractice)
admin.site.register(Sector)
admin.site.register(PYME)
admin.site.register(Autoevaluation)
admin.site.register(Answer)
