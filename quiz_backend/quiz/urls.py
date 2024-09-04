# quiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('results/', views.QuizResultList.as_view()),
]
