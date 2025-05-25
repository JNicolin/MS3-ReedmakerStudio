from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:reed_pk>/', views.event_create, name='event_create'),
    path('update/<int:pk>/', views.event_update, name='event_update'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),
]