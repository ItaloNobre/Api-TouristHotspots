from django.contrib import admin

from comments.actions import approved_comments, disapprove_comments
from .models import Comment

class comment_admin(admin.ModelAdmin):
    list_display = ['user','date','okay']
    actions = [disapprove_comments,approved_comments]

admin.site.register(Comment,comment_admin)