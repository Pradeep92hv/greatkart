from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("hiii")
    return render(request,'home.html')
