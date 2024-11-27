from django.urls import path

from task.views import (
    TodoListView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCreateView,
    TodoCompleteView,
    TodoUndoView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="task-list"),
    path("todos/create/", TodoCreateView.as_view(), name="task-create"),
    path("todos/<int:pk>/update/", TodoUpdateView.as_view(), name="task-update"),
    path("todos/<int:pk>/delete/", TodoDeleteView.as_view(), name="task-delete"),
    path("todos/<int:pk>/complete/", TodoCompleteView.as_view(), name="task-complete"),
    path("todos/<int:pk>/undo/", TodoUndoView.as_view(), name="task-undo"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "task"
