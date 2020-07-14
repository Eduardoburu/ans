from django.urls import path
from .views import Company_Law_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list', Company_Law_ListView.as_view(), name='companylaw_paper_list'), 
    path('2019_November_economics', November_2019View.as_view(), name='companylaw2019_November'),
    path('2019_May_economics', May_2019View.as_view(), name='companylaw2019_May'),
    path('2018_November_economics', November_2018View.as_view(), name='companylaw2018_November'),
]