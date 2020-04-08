from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Sector, PYME, Autoevaluation, Macroprocess, Process, Answer, SpecificPractice, GeneralPractice, Archive, FinancesInformation

admin.site.register(Macroprocess)
admin.site.register(Process)
admin.site.register(SpecificPractice)
admin.site.register(GeneralPractice)
admin.site.register(Sector)
admin.site.register(Autoevaluation)
admin.site.register(Answer)

class PYMEInline(admin.StackedInline):
    model = PYME
    can_delete = False
    verbose_name_plural = 'PYME'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PYMEInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
