from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Taxation_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "taxation/taxation_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "taxation/2019_November_taxation.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "taxation/2019_May_taxation.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "taxation/2018_November_taxation.html")