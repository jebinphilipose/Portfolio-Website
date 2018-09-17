from django.contrib import admin
from .models import Degree, Skill, Summary, Project

admin.site.register(Summary)
admin.site.register(Skill)
admin.site.register(Degree)
admin.site.register(Project)
