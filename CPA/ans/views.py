from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/home.html")
    

class CpaView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/cpa_landing.html")


class PartoneView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/cpa_partone.html")


class ParttwoView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/cpa_parttwo.html")

class PartthreeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/cpa_partthree.html")
