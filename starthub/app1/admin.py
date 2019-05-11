# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import Startup, Founder, Investor, Application

# Register your models here.
admin.site.register(Startup)
admin.site.register(Founder)
admin.site.register(Investor)
admin.site.register(Application)
