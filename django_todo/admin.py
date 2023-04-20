from django.contrib import admin
from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "checked"]
    actions = ["mark_done"]

    @admin.action(description="Mark as Done")
    def mark_done(self, request, queryset):
        queryset.update(checked=True)
