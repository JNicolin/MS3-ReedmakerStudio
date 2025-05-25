from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:reed_pk>/', views.repertoire_create, name='repertoire_create'),
    path('update/<int:pk>/', views.repertoire_update, name='repertoire_update'),
    path('delete/<int:pk>/', views.repertoire_delete, name='repertoire_delete'),
]