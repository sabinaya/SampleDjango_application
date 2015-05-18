from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
	return HttpResponse("Welcome to the website ....<br/><button id='machine'>Calculator</button>")
	
def calc_page(request):
	return HttpResponse("hello")
