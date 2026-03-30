from django.contrib import admin

from MainApp.models import Comment, Snippet

# Register your models here.
admin.site.register([Snippet, Comment])