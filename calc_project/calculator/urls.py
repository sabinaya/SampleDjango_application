from django.conf.urls import patterns, url
from calculator import views

urlpatterns = patterns('',
	url(r'^machine/', views.calc_page, name='calc_page'),
	url(r'^main/', views.main_page, name='main_page'))