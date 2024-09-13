from django.contrib import admin
from django.urls import path
from . import views
from .views import ShortenerListView

app_name = "shortener"

urlpatterns = [
    path("", ShortenerListView.as_view(), name="shorten"),
]
