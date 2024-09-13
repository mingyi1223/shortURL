from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    html = TemplateResponse(request, "home.html")
    return HttpResponse(html.render())


class ShortenerListView(APIView):
  def get(self, request, format=None):
    usernames = [user.username for user in User.objects.all()]
    return Response(usernames)
