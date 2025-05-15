from django.urls import path
from . import views

urlpatterns = [
    path('', views.reed_list, name='reed_list'),
    path('reed/<int:pk>/', views.reed_detail, name='reed_detail'),
    path('reed/new/', views.reed_create, name='reed_create'),
    path('reed/<int:pk>/edit/', views.reed_update, name='reed_update'),
    path('reed/<int:pk>/delete/', views.reed_delete, name='reed_delete'),
]