from django.urls import path
from . import views

urlpatterns = [ 
    path('detail/<int:pk>/', views.board_detail), # 숫자형을 받을거고 pk로 받겠다
    path('list/', views.board_list),
    path('write/', views.board_write),
   
]

