from django.shortcuts import render, redirect
from django.http import request
from .models import *
from .forms import *
# Create your views here.


def home(request):
    allMovies = Movie.objects.all()
    context = {
        "movies": allMovies,
    }
    return render(request, 'main/index.html/', context)


def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        "movie": movie
    }
    return render(request, 'main/details.html', context)


# add movies
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = MovieForm(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")

            else:
                form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movies"})
        else:
            return redirect("main:home")

    return redirect("accounts:login")


def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)

            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:details", id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit Movie"})
        else:
            return redirect("main:home")

    return redirect("accounts:login")


def delete_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie = Movie.objects.get(id=id)

            movie.delete()
            return redirect("main:home")
        else:
            return redirect("main:home")

    return redirect("accounts:login")
