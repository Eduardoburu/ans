from django.urls import path
from .views import Financialmanagement_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list', Financialmanagement_ListView.as_view(), name='financialmanagement_paper_list'),
    path('2019_November_entrepreneurship', November_2019View.as_view(), name='financialmanagement2019_November'),
    path('2019_May_entrepreneurship', May_2019View.as_view(), name='financialmanagement2019_May'),
    path('2018_November_entrepreneurship', November_2018View.as_view(), name='financialmanagement2018_November'),
]