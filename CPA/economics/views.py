from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Economics_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "economics/economics_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "economics/2019_November_economics.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "economics/2019_May_economics.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "economics/2018_November_economics.html")

