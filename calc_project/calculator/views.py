from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def main_page(request):
	return render(request, 'calculator/main_page.html')

def calc_page(request):
	return render(request, 'calculator/calc_page.html')
