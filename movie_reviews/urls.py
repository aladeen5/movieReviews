from django.urls import path

from . import views

app_name = 'movie_reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('<int:movie_id>', views.reviews, name='reviews'),
    path('<int:movie_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', views.deletereview, name='deletereview'),
]