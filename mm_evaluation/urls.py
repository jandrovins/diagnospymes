from django.urls import path

from . import views

app_name = 'mm_evaluation'
urlpatterns = [
        path('', views.Autoevaluation.as_view(), name='autoevaluation'),
        path('save_process_score/', views.save_process_score(), name='save_process_score'),

]
