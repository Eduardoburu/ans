from django.urls import path
from .views import Economics_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list', Economics_ListView.as_view(), name='economics_paper_list'),
    path('2019_November_economics', November_2019View.as_view(), name='economics2019_November'),
    path('2019_May_economics', May_2019View.as_view(), name='economics2019_May'),
    path('2018_November_economics', November_2018View.as_view(), name='economics2018_November'),
]