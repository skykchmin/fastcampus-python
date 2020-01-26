from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id: #유저가 있으면 사용자 정보를 가져오기 
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username) #모델에서 유저네임을 출력
        
    return HttpResponse('Home!')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})   

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def register(request): #등록화면 장고에 등록하기
    # 웹사이트로 직접 url로 들어오는 경우, 등록버튼을 통해 들어오는 경우를 구분도 해야되기 때문에
    # GET 으로 들어왔을때 페이지로 전달, POST로 들어왔을 때 페이지로 전달
    if request.method == 'GET': 
        return render(request, 'register.html') #반환하고 싶은 html을 반환
    elif request.method == 'POST':
        username = request.POST.get('username', None) #html로부터 name 값으로 값들이 전달됨
        password = request.POST.get('password', None) #html로부터 name 값으로 값들이 전달됨
        re_password = request.POST.get('re-password', None) #html로부터 name 값으로 값들이 전달됨
        useremail = request.POST.get('useremail', None)

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser( #객체를 만들고
                username = username,
                password = make_password(password), # make_password를 통해 해쉬를 통해 암호화가 된다
                useremail = useremail
            ) 

            fcuser.save() #객체를 세이브하고 데이터베이스에 생성이 되는지

        return render(request, 'register.html', res_data) #반환하고 싶은 html을 반환, res_data는 에러메시지를 전달하기 위해서 
   

