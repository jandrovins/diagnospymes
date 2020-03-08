from django.urls import path

from . import views

app_name = 'mm_evaluation'
urlpatterns = [
        path('', views.Autoevaluation.as_view()),
]
