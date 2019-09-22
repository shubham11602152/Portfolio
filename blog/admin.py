from django.contrib import admin
from .models import Category, Post


# inline class.
class InLinePost(admin.StackedInline):
    model = Post

# created class to customize what is
# shown on admin page.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified', ]
    # list_display_links = ['created_on']
    list_filter = ['created_on', ]
    # list_editable = ['title', ]
    search_fields = ['title', ]
    fields = (
        'title',
        'body',
        'categories',
    )
    pass


class CategoryAdmin(admin.ModelAdmin):
    # inlines = [InLinePost]
    list_display = ['name', ]
    pass


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
