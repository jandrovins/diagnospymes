from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views


app_name = 'mm_evaluation'
urlpatterns = [
        # This URL points to the home page
        path('', views.IndexView.as_view(), name='index'),
        # This URL will redirect to the first created, but not completed, autoevaluation for the PYME who accesses it
        path('empezar_o_continuar_autoevaluacion/', views.begin_or_continue_autoevaluation, name='begin_or_continue_autoevaluation'),
        # This URL points to the page where the autoevaluation is scored
        path('autoevaluacion/<int:pk>/', views.AutoevaluationView.as_view(), name='autoevaluation'),
        # This URL is only accessed when scoring a process on an autoevaluation, and is accessed from the autoevaluation page
        path('<int:process_id>/<int:autoevaluation_id>/guardar_respuesta/', views.AutoevaluationView.as_view(), name='save_answer'),

        # The following are subsections of home page
        path('mision/', views.Mission.as_view()),
        path('nosotros/', views.AboutUs.as_view()),
        path('vision/', views.Vision.as_view()),
        path('metodologia/', views.Metodology.as_view()),
        path('requisitos/', views.Requirements.as_view()),
        path('instrucciones/', views.Instructions.as_view()),
        path('recursos/', views.Resources.as_view()),

        # This URL points to the page where the autoevaluations of the PYME accessing it will be displayed
        path('resultados/', views.PreviousResults.as_view(), name='results'),
        # This URL points to the result view of each autoevaluation
        path('autoevaluacion/resultado/<int:pk>/', views.ResultDetail.as_view(), name='autoevaluation_result'),

        # The following URLs are used to handle authentication functionalities
        path('registro/', views.registration, name='registration'),
        path('registro_exitoso/', views.SuccessfulRegistrationView.as_view(), name='successful_registration'),
        path('acceso_denegado/', views.AccessDeniedView.as_view(), name='denied_access'),
        path('login/', auth_views.LoginView.as_view(), name="login"),
        path('logout/', auth_views.logout_then_login, name="logout"),
        path('cambiar_contraseña/', auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('mm_evaluation:password_change_done')
            ),
            name="password_change"),
        path('contraseña_cambiada/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
        ]
