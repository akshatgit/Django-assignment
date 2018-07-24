from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('boards/', views.BoardList.as_view()),
    path('tl/', views.TLList.as_view()),
    path('card/', views.CardList.as_view()),
    path('auth/', include('rest_framework.urls')),
    # ex: /polls/5/
    path('<int:pk>/', views.BoardDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/(P<int:pk>)/', views.UserDetail.as_view()),
    # ex: /polls/5/results/
    # path('<int:board_id>//', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
