from django.urls import path
from . import views

app_name = 'auth'
urlpatterns = [
        path('signin', views.signin, name='signin'),
        path('signout', views.signout, name='signout'),
        path('register', views.register, name='register'),
]