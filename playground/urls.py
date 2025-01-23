from django.urls import path
from . import views


# URL Configurations
urlpatterns= [
    path('playground/hello',views.say_hello)
]