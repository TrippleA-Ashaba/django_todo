from django.contrib import admin
from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "done", "date_created"]
    actions = ["mark_done", "mark_not_done"]

    @admin.action(description="Mark as Done")
    def mark_done(self, request, queryset):
        queryset.update(done=True)

    @admin.action(description="Mark as Not Done")
    def mark_not_done(self, request, queryset):
        queryset.update(done=False)
