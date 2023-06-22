from django.shortcuts import render
from django.views import generic
from  django.http import HttpResponse
# Create your views here.

def index_page(request):
    return render(request, 'index.html')

# Create your views here.
