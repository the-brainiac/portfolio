from django.contrib import admin

# Register your models here.

from .models import Project, Tag, Resume, Profile

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Resume)
admin.site.register(Profile)