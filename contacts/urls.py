from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_contact, name = 'add_contact'),
    path('get/<str:number>/', views.get_contact, name = 'get_contact'),
]