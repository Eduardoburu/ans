from django.urls import path
from .views import Fa_questionsView
from . import views



urlpatterns = [
    path('financial_accounting', Fa_questionsView.as_view(), name='financial_accounting'),
]