from django.contrib import admin

# Register your models here.

from .models import Post, Update


class UpdateInLine(admin.TabularInline):
    model = Update
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        UpdateInLine,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Update)

