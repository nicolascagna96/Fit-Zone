from django.shortcuts import render
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

# Contact form


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been sent sucesfully !'
                )
            return HttpResponseRedirect('/contact?submitted=True')
        else:
            messages.error(
                request, 'There was a problem sending your message. \
                    Please try again.')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
