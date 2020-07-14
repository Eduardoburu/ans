from django.urls import path
from .views import Taxation_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list', Taxation_ListView.as_view(), name='taxation_paper_list'),
    path('2019_November_taxation', November_2019View.as_view(), name='taxation2019_November'),
    path('2019_May_taxation', November_2019View.as_view(), name='taxation2019_May'),
    path('2018_November_taxation', November_2018View.as_view(), name='taxation2018_November'),
]
