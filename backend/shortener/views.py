from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from .serializer import SiteSerializer
from .models import Site
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class ShortenerCreateView(APIView):
    def post(self, request):
        serializer = SiteSerializer(data=request.data)

        if serializer.is_valid():
            long_url = serializer.validated_data["long"]

            short_code = generate_short_code()
            base_url = settings.BASE_URL
            short_url = base_url + short_code

            while Site.objects.filter(short=short_url).exists():
                short_code = generate_short_code()
                short_url = base_url + short_code

            site_instance = Site.objects.create(long=long_url, short=short_url)

            return Response(SiteSerializer(site_instance).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortenerRedirectView(View):
    def get(self, request, short_code, *args, **kwargs):
        short_url = settings.BASE_URL + short_code
        site_instance = get_object_or_404(Site, short=short_url)
        return redirect(site_instance.long)
