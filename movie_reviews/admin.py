from django.contrib import admin
from .models import Movie, Review
admin.site.register(Review)

# Register your models here.
admin.site.register(Movie)