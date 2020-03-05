from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    # -는 역순을 의미
    # 모든 게시물을 가지고 올껀데 역순이여서 최신순으로 가져올 것이다. 
    return render(request, 'board_list.html', {'boards': boards})