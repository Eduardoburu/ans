from django.urls import path
from .views import Managementaccounting_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list/MA', Managementaccounting_ListView.as_view(), name='managementaccounting_paper_list'),
    path('2019_November_managementaccounting', November_2019View.as_view(), name='managementaccounting2019_November'),
    path('2019_May_managementaccounting', May_2019View.as_view(), name='managementaccounting2019_May'),
    path('2018_November_managementaccounting', November_2018View.as_view(), name='managementaccounting2018_November'),
]