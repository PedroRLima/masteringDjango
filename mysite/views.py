from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import datetime


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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})
