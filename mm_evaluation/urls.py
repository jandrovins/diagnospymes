from django.urls import path

from . import views

app_name = 'mm_evaluation'
urlpatterns = [
        path('autoevaluation/', views.AutoevaluationView.as_view(), name='autoevaluation'),
        path('<int:pk>/save_answer/', views.save_answer, name='save_answer'),
        path('process_already_answer/', views.ProcessAlreadyAnswerView.as_view(), name='process_already_answer'),
]
