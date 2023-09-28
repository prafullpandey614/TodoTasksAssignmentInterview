from rest_framework.serializers import ModelSerializer
from .models import TodoItems,ListItem 

class ListItemSerializer(ModelSerializer):
    class Meta:
        model = ListItem
        fields = "__all__"
        
class TodoTaskItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItems
        fields = "__all__"
        