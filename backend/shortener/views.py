from django.shortcuts import render
from .models import Site
from serializer import SiteSerializer

# Create your views here.

class ShortenerListAPIView(ListAPIView):
  queryset = Site.objects.all()
  serializer_class = SiteSerializer