from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from time import sleep

from .models import Greeting

# Create your views here.
@csrf_exempt
def index(request):
    #sleep(1000000000000)
    return HttpResponse(status=400)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
