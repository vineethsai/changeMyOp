from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('users/<int:user_id>', views.specificUser, name='Profile'),
    path('opinions', views.opinions, name='Opinions'),
    path('opinions/<int:op_id>', views.specific_opinions, name='Specific Opinions')
]
