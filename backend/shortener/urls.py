from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", ShortenerListView().as_view(), name="all"),

]
