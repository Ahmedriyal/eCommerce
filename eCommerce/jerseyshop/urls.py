from django.urls import path, include

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('club/', views.club, name="club"),
	path('country/', views.country, name="country"),
]