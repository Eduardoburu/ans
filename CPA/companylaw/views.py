from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Company_Law_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "companylaw/companylaw_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "companylaw/2019_November_companylaw.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "companylaw/2019_May_companylaw.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "companylaw/2018_November_companylaw.html")

