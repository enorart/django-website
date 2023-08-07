from django.urls import path

from .views import index, add_collection, add_task, get_task, delete_task, delete_collection

urlpatterns = [
    path('',index, name="tasks-index"),
    path('add-collection/',add_collection, name="tasks-add-collection"),
    path('add-task/',add_task,name="tasks-add-task"),
    path('get-task/<str:collection_slug>/',get_task,name="tasks-get-task"),
    path('delete-task/<int:task_pk>',delete_task,name="tasks-delete-task"),
    path('delete-collection/<str:collection_slug>',delete_collection,name="tasks-delete-collection")
]