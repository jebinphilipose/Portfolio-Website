from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Degree, Skill, Summary, Project
from .forms import ContactForm


def home(request):
    skills = Skill.objects.all()
    degrees = Degree.objects.all()
    summary = Summary.objects.first()
    projects = Project.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            subject = "You have a new message from {}: <{}>" \
                      .format(name, email)
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email]
            contact_message = "Sent by: %s\n\nEmail: %s\n\nMessage:\n\n%s" \
                              % (name, email, message)
            send_mail(subject,
                      contact_message,
                      from_email,
                      [to_email],
                      fail_silently=False)
            return JsonResponse({
                'success': True,
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })

    return render(request, 'portfolio/index.html', {'skills': skills,
                                                    'degrees': degrees,
                                                    'summary': summary,
                                                    'projects': projects,
                                                    'form': form})
