from django.shortcuts import render, redirect
from .models import Movie, Director
from .forms import MovieForm, MovieDirectorForm, DirectorForm

# Create your views here.
def home(request):
    return render(request, 'main/index.html')
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        # No validation. Risky!
        form.save()
        return redirect('show_movies')
    else:
        form = MovieForm()
        return render(request, 'movie/add.html',{'title':'movie','form':form})
def add_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        # No validation. Risky!
        form.save()
        return redirect('show_directors')
    else:
        form = DirectorForm()
        return render(request, 'movie/add.html',{'title':'director','form':form})
# Ref: https://docs.djangoproject.com/en/2.1/topics/forms/#the-view
def edit_director(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        form = MovieDirectorForm(request.POST,instance=movie)
        form.save()
        return redirect('show_movies')
    else:
        form = MovieDirectorForm()
        return render(request, 'movie/edit_director.html',{'form':form})
def show_movies(request):
    movies=Movie.objects.all()
    return render(request,'movie/show_movies.html',{'movies':movies})
def show_directors(request):
    directors=Director.objects.all()
    return render(request,'movie/show_directors.html',{'directors':directors})





