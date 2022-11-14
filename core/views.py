from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            print('Sent message')
            print('Client {} with email {}'.format(name, email))
            print('Sent message has subject {}'.format(subject))
            print('Message :\n {}'.format(content))

            messages.success(request, 'Sent message with sucess!')
            form = ContactForm()
        else:
            messages.error(request, 'Error with message')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')
