from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Fa_listView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialAccounting/fa_list.html")


class Fa2019_novView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialAccounting/2019_fa_one.html")


class Fa2018_novView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "financialAccounting/2018_fa_one.html")