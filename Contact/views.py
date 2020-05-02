from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Contact.forms import ContactForm
from Contact.models import Contact


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
