from django.urls import path, include

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('club/', views.club, name="club"),
	path('country/', views.country, name="country"),
	path('search_results/', views.search_results, name="search_results"),
	path('country/<int:jersey_id>/', views.national_jersey_details, name="national_jersey_details"),
	path('club/<int:jersey_id>/', views.club_jersey_details, name="club_jersey_details"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
]