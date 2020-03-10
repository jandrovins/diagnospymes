from django.urls import path

from . import views


app_name = 'mm_evaluation'
urlpatterns = [
    path('autoevaluacion/', views.AutoevaluationView.as_view(), name='autoevaluation'),
    path('<int:pk>/guardar_respuesta/', views.AutoevaluationView.as_view(), name='save_answer'),
    path('proceso_ya_respondido/', views.ProcessAlreadyAnswerView.as_view(), name='process_already_answer'),
    path('', views.IndexView.as_view(), name='index'),
    path('mision/', views.Mission.as_view()),
    path('nosotros/', views.AboutUs.as_view()),
    path('vision/', views.Vision.as_view()),
    path('metodologia/', views.Metodology.as_view()),
    path('requisitos/', views.Requirements.as_view()),
    path('instrucciones/', views.Instructions.as_view()),
    path('recursos/', views.Resources.as_view()),
    path('resultados/', views.PreviousResults.as_view(), name='results'),
    path('resultados/<int:pk>/', views.ResultDetail.as_view(), name='result_detail'),
]
