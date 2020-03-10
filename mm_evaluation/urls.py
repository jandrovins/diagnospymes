from django.urls import path

from . import views


app_name = 'mm_evaluation'
urlpatterns = [
    path('autoevaluacion/', views.AutoevaluationView.as_view(), name='autoevaluation'),
    path('<int:pk>/save_answer/', views.AutoevaluationView.as_view(), name='save_answer'),
    path('process_already_answer/', views.ProcessAlreadyAnswerView.as_view(), name='process_already_answer'),
    path('', views.IndexView.as_view(), name='index'),
    path('resultados/', views.PreviousResults.as_view(), name='resultados'),
    path('resultados/<int:pk>/', views.ResultDetail.as_view(), name='detalleResultado' )
]
