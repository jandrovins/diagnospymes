from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Answer,
    Archive,
    Autoevaluation,
    FinancesInformation,
    GeneralPractice,
    Macroprocess,
    Process,
    PYME,
    Sector,
    SpecificPractice,
)

# Edit the following models in admin page
admin.site.register(Macroprocess)
admin.site.register(Process)
admin.site.register(SpecificPractice)
admin.site.register(GeneralPractice)
admin.site.register(Sector)
admin.site.register(Autoevaluation)
admin.site.register(Answer)

# Auxiliary class to edit PYME objects in 'edit User' page
class PYMEInline(admin.StackedInline):
    model = PYME
    can_delete = False
    verbose_name_plural = "PYME"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PYMEInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
