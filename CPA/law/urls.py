from django.urls import path
from .views import Law_ListView, November_2019View, May_2019View, November_2018View




urlpatterns = [
    path('list', Law_ListView.as_view(), name='law_paper_list'),
    path('2019_November_Law-One', November_2019View.as_view(), name='law2019_November'),
    path('2019_May_Law-One', November_2019View.as_view(), name='law2019_May'),
    path('2018_November_Law-One', November_2018View.as_view(), name='law2018_November'),
]