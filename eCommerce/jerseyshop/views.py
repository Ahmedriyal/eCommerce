from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import ClubJerseyDetails, NTJerseyDetails
from django.core.paginator import Paginator
from .filters import SearchFilter


# Create your views here.

def home(request):
    jerseys = ClubJerseyDetails.objects.all()[:4]
    NTjerseys = NTJerseyDetails.objects.all()[:4]

    return render(request, 'html/home.html', {'jerseys': jerseys, 'NTjerseys': NTjerseys})


def club(request):
    jerseys = ClubJerseyDetails.objects.all()
    paginator = Paginator(jerseys, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/club.html', {'page_obj': page_obj})
    # return render(request, 'html/club.html', {'jerseys': jerseys})


def country(request):
    NTjerseys = NTJerseyDetails.objects.all()
    paginator = Paginator(NTjerseys, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'html/country.html', {'page_obj': page_obj})
    # return render(request, 'html/country.html', {'NTjerseys': NTjerseys})


def search_results(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        page_obj = ClubJerseyDetails.objects.all().filter(title__icontains=searched)
        page_obj1 = NTJerseyDetails.objects.all().filter(title__icontains=searched)

        return render(request, 'html/search_results.html',
                      {'searched': searched, 'page_obj': page_obj, 'page_obj1': page_obj1})
    else:
        return render(request, 'html/search_results.html', {})


def national_jersey_details(request, jersey_id):
    jersey = NTJerseyDetails.objects.get(pk=jersey_id)

    return render(request, 'html/national_jersey_details.html', {'jersey': jersey})

def club_jersey_details(request, jersey_id):
    jersey = ClubJerseyDetails.objects.get(pk=jersey_id)

    return render(request, 'html/club_jersey_details.html', {'jersey': jersey})