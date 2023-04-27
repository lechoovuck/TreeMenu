from django.shortcuts import render
from django.views.generic import View


class Index(View):
    def get(self, request, params=None):
        return render(request, 'main/index.html', {
            'title': 'Home',
        })
