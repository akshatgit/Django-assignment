from django.db import models
from django.utils import timezone

class Board(models.Model):
    owner = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=timezone.now())
    def __str__(self):
        return self.name


class TaskList(models.Model):
    board = models.ForeignKey(Board, related_name="task_list",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Card(models.Model):
    task_list = models.ForeignKey(TaskList, related_name="card", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name
