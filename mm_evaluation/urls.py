from django.urls import path

from . import views


app_name = 'mm_evaluation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('autoevaluation/', views.Autoevaluation.as_view()),
    path('mision/', views.Mission.as_view()),
    path('nosotros/', views.AboutUs.as_view()),
    path('vision/', views.Vision.as_view()),
    path('metodologia/', views.Metodology.as_view()),
    path('requisitos/', views.Requirements.as_view()),
    path('instrucciones/', views.Instructions.as_view()),
    path('recursos/', views.Resources.as_view()),
]
