from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListApiView.as_view()),
    path('ads/', AdListApiView.as_view()),
    path('ads/<int:pk>/', AdDetailApiView.as_view()),
]