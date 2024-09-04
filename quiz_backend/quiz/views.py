# from django.shortcuts import render

# # Create your views here.
# quiz/views.py

from rest_framework import generics
from .models import Category, Question, Answer, QuizResult
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer, QuizResultSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class QuizResultList(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
