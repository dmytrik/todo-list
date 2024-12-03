from django.contrib import admin

from task.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("deadline",)


admin.site.register(Tag)
