from django.urls import path
from .views import *

urlpatterns = [
    path('add-list/', ListItemListCreateView.as_view(), name='list-item-list-create'),
    path('list_items/<int:pk>/', ListItemRetrieveUpdateDestroyView.as_view(), name='list-item-retrieve-update-destroy'),
    path('todo_items/', TodoItemsListCreateView.as_view(), name='todo-items-list-create'),
    path('todo_items/<int:pk>/', TodoItemsRetrieveUpdateDestroyView.as_view(), name='todo-items-retrieve-update-destroy'),
    path('list_items/<int:list_id>/tasks/', TaskListByListItemView.as_view(), name='task-list-by-list-item'),
]
