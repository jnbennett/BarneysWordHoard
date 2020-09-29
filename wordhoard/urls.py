from django.urls import path, include, reverse_lazy
from rest_framework import routers, serializers, viewsets 
from django.views.generic import TemplateView
from . import views 

app_name = 'wordhoard'

router = routers.DefaultRouter()
router.register(r'word', views.WordViewSet, basename='word')
router.register(r'group', views.GroupViewSet, basename='group')
urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('api/', include(router.urls)),
]