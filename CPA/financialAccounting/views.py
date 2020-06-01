from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Fa_questionsView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "ans/fa_questions.html")