from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Law_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "law/law_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "law/2019_November_Law_one.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "law/2019_May_Law_one.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "law/2018_November_Law_one.html")