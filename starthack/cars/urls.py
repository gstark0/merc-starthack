from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

urlpatterns = [
    path('welcome/', views.facial_recognition),
]

urlpatterns = format_suffix_patterns(urlpatterns)