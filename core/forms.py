from django import forms
from django.core.mail import EmailMessage
from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    subject = forms.CharField(label="Subject", max_length=120)
    content = forms.CharField(label="Content", widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        content = self.cleaned_data['content']

        content_mail = f'Name:{name}\nE-mail:{email}\nSubject:{subject}\nMessage:\n{content}'
        mail = EmailMessage(
            subject='Message that it sent by system',
            body=content_mail,
            from_email='leonardojs@protonmail.com',
            to=['leonardojs@protonmail.com', ],
            headers={'Reply-To': email}
        )

        mail.send()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']