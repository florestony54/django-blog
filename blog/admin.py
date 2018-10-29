from django.contrib import admin
from blog.models import Post, Comment
from tinymce.widgets import TinyMCE
# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
