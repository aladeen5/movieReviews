from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Home page."""
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    context = {'name': 'Kate Baraza', 'searchTerm':searchTerm, 'movies': movies}
    return render(request, 'movie_reviews/index.html', context)

def about(request):
    return HttpResponse('<h1>Welcome to About Page.</h1>')
def signup(request):
    email = request.GET.get('email')
    return render(request, 'movie_reviews/signup.html',{'email':email})

def reviews(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie_reviews/reviews.html' ,
                  {'movie':movie, 'reviews': reviews})

@login_required()
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'movie_reviews/createreview.html',
                      {'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('movie_reviews:reviews', newReview.movie.id)
        except ValueError:
            return render(request, 'movie_reviews/createreview.html',
                          {'form': ReviewForm(), 'error': 'bad data passed in '})

@login_required()
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie_reviews/updatereview.html',
                      {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('movie_reviews:reviews', review.movie.id)
        except ValueError:
            return render(request, 'movie_reviews/updatereview.html',
                          {'review': review,'form':form, 'error':'Bad data in form'})
@login_required()
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('movie_reviews:reviews', review.movie.id)