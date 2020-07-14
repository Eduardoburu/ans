from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Financialmanagement_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialmanagement/financialmanagement_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialmanagement/2019_November_financialmanagement.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialmanagement/2019_May_financialmanagement.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialmanagement/2018_November_financialmanagement.html")
