from django.urls import path
from .views import ShortenerCreateView, ShortenerRedirectView

app_name = "shortener"

urlpatterns = [
    path("", ShortenerCreateView.as_view(), name="create"),
    path("<str:short_code>/", ShortenerRedirectView.as_view(), name="redirect")
]
