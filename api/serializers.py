from rest_framework import serializers
from django.utils import timezone
from api.models import Board, TaskList, Card
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'boards')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','name','description','task_list')

class TaskListSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True, many=True)
    class Meta:
        model = TaskList
        fields = ('id','board','name','card')

class BoardSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer(read_only=True,many=True)
    # print(task_lists)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Board
        fields = ('id','name','pub_date','task_list','owner')
