from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello World!")


def home_page(request):
    time = datetime.datetime.now()
    html_response = "It's now %s." % time
    return HttpResponse(html_response)
