from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1> Home </h1>')

def about_us(request):
	return HttpResponse('<h1> About Us </h1>')

