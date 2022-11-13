from django.contrib import admin
from blog.models import Tag, Post
admin.site.register(Tag)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)    