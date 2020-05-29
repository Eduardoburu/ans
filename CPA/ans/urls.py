from django.urls import path
from .views import HomeView, CpaView
from . import views



urlpatterns = [
    path('', HomeView.as_view(), name='ans-home'),
    path('cpa', CpaView.as_view(), name='cpa-home'),
]