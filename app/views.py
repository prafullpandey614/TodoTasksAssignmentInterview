from rest_framework import generics
from .models import ListItem, TodoItems
from .serializers import ListItemSerializer, TodoTaskItemSerializer

class ListItemListCreateView(generics.ListCreateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

class ListItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

class TodoItemsListCreateView(generics.ListCreateAPIView):
    queryset = TodoItems.objects.all()
    serializer_class = TodoTaskItemSerializer

class TodoItemsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItems.objects.all()
    serializer_class = TodoTaskItemSerializer

class TaskListByListItemView(generics.ListAPIView):
    serializer_class = TodoTaskItemSerializer

    def get_queryset(self):
        list_id = self.kwargs.get('list_id')
        return TodoItems.objects.filter(list_item_id=list_id)
    
    