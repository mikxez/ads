from django.urls import path
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('create/', views.ad_create, name='ad_create'),
    path('<int:pk>/edit/', views.ad_update, name='ad_update'),
    path('<int:pk>/delete/', views.ad_delete, name='ad_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

