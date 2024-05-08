from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signupaccount', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
]