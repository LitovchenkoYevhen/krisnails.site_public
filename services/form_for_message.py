from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from services.forms import ContactForm


def make_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['subject'] = form.cleaned_data['telephone'] + ' | ' + form.cleaned_data['name'] \
                                           + ' | ' + form.cleaned_data['email']
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'krisnails@ukr.net',
                             ('litovchenkoyevhen@gmail.com',))
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('services:contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка ввода')
    else:
        form = ContactForm()
    return form
