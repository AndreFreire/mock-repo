from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response


from .models import Greeting

# Create your views here.
def index(request):
    return Response(content, status=status.HTTP_404_NOT_FOUND)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
