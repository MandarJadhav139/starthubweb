# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.


class AppManager(models.Manager):
    def create_application(self, name, email, github, resume):
        application = self.create(
            name=name, email=email, github=github, resume=resume)
        # do something with the book
        return application


class Startup(models.Model):
    logo = models.ImageField(upload_to='logos')

    name = models.CharField(unique=True, max_length=30)
    domain = models.CharField(max_length=20)
    networth = models.CharField(max_length=20)
    location = models.CharField(max_length=15)
    site = models.URLField()
    slug = models.SlugField(allow_unicode=True, unique=True, default='x')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Application(models.Model):
    name = models.CharField(max_length=30)
    github = models.URLField(max_length=50)
    startup = models.ForeignKey(
        Startup, on_delete=models.DO_NOTHING, null=True, related_name='applications')
    resume = models.ImageField(upload_to='resumes')
    email = models.EmailField()
    objects = AppManager()

    def __str__(self):
        return self.name


class Investor(models.Model):
    startup = models.ForeignKey(
        Startup, on_delete=models.DO_NOTHING, null=True, related_name='investors')
    profilepic = models.ImageField(upload_to='investors')
    name = models.CharField(max_length=30)
    investment = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Founder(models.Model):
    startup = models.ForeignKey(
        Startup, on_delete=models.DO_NOTHING, null=True, related_name='founders')
    profilepic = models.ImageField(upload_to='founders')
    name = models.CharField(max_length=30)
    post = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
