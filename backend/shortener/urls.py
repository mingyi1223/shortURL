
from django.urls import path
from .views import ShortenerCreateView, ShortenerRetrieveView

app_name = "shortener"

urlpatterns = [
    path("", ShortenerCreateView.as_view(), name="create"),
    path("<str:short_code>/",ShortenerRetrieveView.as_view(),name="retrieve",)
]