from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm

def board_detail(request, pk): # 첫번째 글인지, 두번째 글인지 입력을 받아야함 그래서 pk 필요
    board = Board.objects.get(pk=pk) # pk에 해당하는 글을 가져올 수 있다
    return render(request, 'board_detail.html', {'board': board})

# Create your views here.
def board_write(request): #제목과 내용이 요청되었을 때 작성자 정보까지 저장
    if request.method == 'POST': #글 쓸 때 로그인이 되어있어야함 
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user') #세션을 가져온다
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser #fcuser를 가져와서 사용
            board.save() # 데이터베이스에 저장

            return redirect('/board/list/') #글 작성을 완료할 경우 이동시키기 위해서 
    else:
        form = BoardForm()
   
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    # -는 역순을 의미
    # 모든 게시물을 가지고 올껀데 역순이여서 최신순으로 가져올 것이다. 
    return render(request, 'board_list.html', {'boards': boards})