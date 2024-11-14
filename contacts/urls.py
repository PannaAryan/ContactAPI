from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ContactViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('add/', views.add_contact, name='add_contact'),
    path('get/<str:number>/', views.get_contact, name='get_contact'),
    path('', include(router.urls)),
]
