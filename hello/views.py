from django.shortcuts import render
from django.http import HttpResponse


from .models import Greeting

# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse(status=204)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
