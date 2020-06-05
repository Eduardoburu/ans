from django.urls import path
from .views import Fa2019_novView, Fa_listView, Fa2018_novView
from . import views



urlpatterns = [
    path('2019_November', Fa2019_novView.as_view(), name='financial_accounting'),
    path('2018_November', Fa2018_novView.as_view(), name='2018_FA_Nov'),
    path('fa_questions_list', Fa_listView.as_view(), name='fa_questions_list'),
]