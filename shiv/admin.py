from django.contrib import admin

# Register your models here.

from .models import Project, Tag

admin.site.register(Project)
admin.site.register(Tag)
