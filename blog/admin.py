from django.contrib import admin

from .models import Post

admin.site.site_header = "Kevin Bisner"
admin.site.site_title = "Kevin Bisner"
admin.site.index_title = "Admin | Kevin Bisner"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_on", "updated_on", "published_on")
    readonly_fields = ("published_on",)
    ordering = ("-published_on",)
    date_hierarchy = "created_on"
    empty_value_display = '-NOT-SET-'
