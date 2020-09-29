from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Word, Group 
from .serializers import WordSerializer, GroupSerializer 

class WordViewSet(viewsets.ModelViewSet):
	queryset = Word.objects.all().order_by('word')
	serializer_class = WordSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all().order_by('group')
	serializer_class = GroupSerializer

class HomePageView(TemplateView):
	template_name = "wordhoard/home.html"