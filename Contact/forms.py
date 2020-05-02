from django.forms import ModelForm, Textarea, TextInput, EmailInput

from Contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': Textarea(attrs={"rows": "10", "cols": "50", "class": "form-control"}),
            'name': TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            'email': EmailInput(attrs={"class": "form-control"})
        }
