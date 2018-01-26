from django.shortcuts import render
from django.http import HttpResponse

def indexfinn(request):
	return HttpResponse("<h1>Hello,boy Finn.</h1>")