from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello World!")


def time_now(request):
    time = datetime.datetime.now()
    template = "time_now.html"
    context = {"current_time": time}
    return render(request, template, context)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except Exception as e:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    print("I'm here bitch")
    template = "hours_ahead.html"
    context = {"hour_offset": offset, "next_time": dt}
    return render(request, template, context)
