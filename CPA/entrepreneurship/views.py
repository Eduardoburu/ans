from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Entrepreneurship_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "entrepreneurship/entrepreneurship_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "entrepreneurship/2019_November_entrepreneurship.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "entrepreneurship/2019_May_entrepreneurship.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "entrepreneurship/2018_November_entrepreneurship.html")
