from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
        return HttpResponse("<h1> hello </h1>")

def complain(request):	
	pass
def retakes(request):
	pass
