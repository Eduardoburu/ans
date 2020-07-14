from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Managementaccounting_ListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "managementaccounting/managementaccounting_list.html")

class November_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "managementaccounting/2019_November_managementaccounting.html")

class May_2019View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "managementaccounting/2019_May_managementaccounting.html")


class November_2018View(View):
    def get(self, *args, **kwargs):
        return render(self.request, "managementaccounting/2018_November_managementaccounting.html")

