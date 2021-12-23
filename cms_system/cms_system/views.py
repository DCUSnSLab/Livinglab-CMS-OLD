from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'index.html')
