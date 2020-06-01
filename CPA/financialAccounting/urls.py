from django.urls import path
from .views import Fa2019_novView, Fa_listView
from . import views



urlpatterns = [
    path('2019_November', Fa2019_novView.as_view(), name='financial_accounting'),
    path('fa_questions_list', Fa_listView.as_view(), name='fa_questions_list'),
]