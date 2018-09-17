from django.shortcuts import render
from .models import Degree, Skill, Summary, Project


def home(request):
    skills = Skill.objects.all()
    degrees = Degree.objects.all()
    summary = Summary.objects.first()
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'skills': skills,
                                                    'degrees': degrees,
                                                    'summary': summary,
                                                    'projects': projects})
