from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.models import Board,TaskList,Card
from rest_framework.views import APIView
from api.serializers import BoardSerializer,TaskListSerializer,CardSerializer
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.models import Board
from api.serializers import BoardSerializer
from rest_framework import mixins
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TLList(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class TLDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,)

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,)


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,)

#
# @api_view(['GET', 'POST'])
# def board(request):
#     """
#     List all board.
#     """
#     if request.method == 'GET':
#         boards = Board.objects.all()
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BoardSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def board_detail(request, pk):
#     """
#     Retrieve, update or delete a board.
#     """
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         return Response(status=404)
#
#     if request.method == 'GET':
#         serializer = BoardSerializer(board)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BoardSerializer(Board, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         board.delete()
#         return Response(status=204)
#
# @api_view(['GET', 'POST'])
# def board_list(request):
#     """
#     List all board, or create a new board.
#     """
#     if request.method == 'GET':
#         boards = Board.objects.all()
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BoardSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

# def board_detail(request, board_id):
#     return HttpResponse("You're looking at board %s." % board_id)
#
# def task_list(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
