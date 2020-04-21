from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms
from django.utils.translation import gettext_lazy as _

from .models import PYME

class PYMERegistrationForm(forms.ModelForm):
    """Form to create PYME information in registration form.

    Inherits from ModelForm, and uses PYME model. This form will hold information related to the PYME model, 
    except for User field, which will be managed using UserRegistrationForm. This localizes `contact_birth_date`. 

    Fields:
        name (forms.CharField):
        sector (forms.ModelChoiceField): displays with a select widget.
        nit (forms.CharField):
        address (forms.CharField):
        phone_number (forms.CharField):
        contact_sex (forms.CharField):
        contact_phone_number (forms.CharField):
        contact_birth_date (forms.DateField): displays with a text widget.
        contact_id_type (forms.CharField): displays with a select widget.
        contact_id_number (forms.CharField):
        contact_time_on_charge (forms.IntegerField):
        contact_education_level (forms.CharField): displays with a select widget.
        terms_conditions_acceptance (forms.BooleanField): display as a click box widget.
        
    """
    class Meta:
        # Create form fields according to fields in PYME model
        model = PYME
        # Do not create a field for User object. In registration page, User form fields are created using UserRegistrationForm defined below
        exclude = ('user',)
        localized_fields = ('contact_birth_date',)
        # Specify labels for each field
        labels = {
            'name': _('Nombre de la empresa'),
            'sector': _('Nombre del sector económico al cual pertenece la empresa'),
            'nit': _('NIT de la empresa'),
            'address': _('Dirección de la empresa'),
            'phone_number': _('Número telefónico de la empresa'),
            'contact_sex': _('Sexo del contacto de la empresa'),
            'contact_phone_number': _('Número telefónico del contacto de la empresa'),
            'Contact_birth_date': _('Fecha de nacimiento del contacto de la empresa'),
            'contact_id_type': _('Tipo del documento del contacto de la empresa'),
            'contact_id_number': _('Número del documento del contacto de la empresa'),
            'contact_time_on_charge': _('Tiempo que lleva a cargo el contacto de la empresa'),
            'contact_education_level': _('Nivel de educación del contacto de la empresa'),
            'terms_conditions_acceptance': _('Aceptación de Términos y Condiciones'),
        }

        

class UserRegistrationForm(UserCreationForm):
    """Form to create User information in registration page.

    Inherits from UserCreationForm, and uses Django's User model. Since `password1` and `password2`
    (i.e. password and password confirmation) are not fields of User model, they are created in this form. 
    Labels for each field are defined in order to display form in spanish.

    Fields:
        username (forms.CharField): username to be created in registration page.
        email (forms.CharField): email to be created in registrtion page.
        first_name (forms.CharField):
        last_name (forms.CharField):
        password1 (forms.CharField): password to be created in registration form.
        password2 (forms.CharField): password confirmation.

    """
    # Predefined error messages
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    # Since password is not a field in User model, one has to create a form field for this
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Ingrese nuevamente su contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        # Create form fields according to fields in PYME model
        model = User
        # Specify User model fields to use
        fields = ('username', 'email', 'first_name', 'last_name',)
        # Specify labels for each field
        labels = {
            'username': _('Nombre de usuario'),
            'email': _('Ingrese el correo electrónico del contacto de la empresa'),
            'first_name': _('Nombres del contacto de la empresa'),
            'last_name': _('Apellidos del contacto de la empresa'),
        }
