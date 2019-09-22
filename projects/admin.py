from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    admin.site.site_header = 'Admin Dashboard'
    list_display = ['title', 'technology', 'image', ]


# Register your models here.
admin.site.register(Project, ProjectAdmin)


# customization Admin Panel.
