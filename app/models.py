from django.db import models

# Create your models here.

class ListItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField(blank=True,null=True)
    created_on  = models.DateTimeField(auto_now_add=True)
    
    #to get proper name I defined str funciton here
    def __str__(self):
        return f"{self.name}"
    
class TodoItems(models.Model):
    list_item = models.ForeignKey(ListItem,on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField(blank=True,null=True)
    created_on  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}  {self.task}"