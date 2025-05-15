from django.urls import path
from . import views

urlpatterns = [
    path('', views.reed_list, name='reed_list'),
    path('<int:pk>/', views.reed_detail, name='reed_detail'),
    path('new/', views.reed_create, name='reed_create'),
    path('<int:pk>/edit/', views.reed_update, name='reed_update'),
    path('<int:pk>/delete/', views.reed_delete, name='reed_delete'),
]
