from django.contrib import admin
from blog.models import Category, Post, Comment, Tag, Photograph


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    ordering = ('-id', 'name',)

admin.site.register(Category, CategoryAdmin)

class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'category', 'title')
    search_fields = ('title', 'content')
    inlines = [CommentInlineAdmin]

admin.site.register(Post, PostAdmin)


admin.site.register(Comment)
admin.site.register(Tag)


admin.site.register(Photograph)