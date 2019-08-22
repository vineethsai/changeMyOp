from django.contrib import admin

from django.contrib import admin
from .models import Opinion, Comment, Like, Dislike

# Register your models here.
admin.site.register(Comment)
admin.site.register(Opinion)
admin.site.register(Like)
admin.site.register(Dislike)
