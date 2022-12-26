from django.contrib import admin
from app.models import job_post

class job_admin(admin.ModelAdmin):
    list_display= ('title', 'discription', 'slug')
    list_filter=('title', 'discription')
    search_fields=['title',]
    fields=('title', "discription")
# Register your models here.
admin.site.register(job_post, job_admin)