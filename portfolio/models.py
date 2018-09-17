from django.db import models


class Summary(models.Model):
    summary = models.TextField()

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'


class Degree(models.Model):
    logo_class = models.CharField(max_length=50)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

    def __str__(self):
        return self.degree


class Skill(models.Model):
    skill = models.CharField(max_length=200)
    progress = models.CharField(max_length=4)

    def __str__(self):
        return self.skill


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    github_link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title
