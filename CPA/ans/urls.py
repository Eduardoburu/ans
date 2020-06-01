from django.urls import path
from .views import HomeView, CpaView, PartoneView, ParttwoView, PartthreeView
from . import views



urlpatterns = [
    path('', HomeView.as_view(), name='ans-home'),
    path('cpa', CpaView.as_view(), name='cpa-home'),
    path('cpa/partone', PartoneView.as_view(), name='cpa-partone'),
    path('cpa/parttwo', PartoneView.as_view(), name='cpa-parttwo'),
    path('cpa/partthree', PartoneView.as_view(), name='cpa-partthree'),
]