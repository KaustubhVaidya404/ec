from django.shortcuts import render
from django.http import HttpResponse

# test view for dashboard
def dashboard(request):
    return HttpResponse("Dashboard view.")
