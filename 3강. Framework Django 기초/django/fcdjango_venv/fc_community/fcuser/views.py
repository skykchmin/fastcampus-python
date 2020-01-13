from django.http import HttpResponse
from django.shortcuts import render
from .models import Fcuser
# Create your views here.

def register(request): #등록화면 장고에 등록하기
    # 웹사이트로 직접 url로 들어오는 경우, 등록버튼을 통해 들어오는 경우를 구분도 해야되기 때문에
    # GET 으로 들어왔을때 페이지로 전달, POST로 들어왔을 때 페이지로 전달
    if request.method == 'GET': 
        return render(request, 'register.html') #반환하고 싶은 html을 반환
    elif request.method == 'POST':
        username = request.POST.get('username') #html로부터 name 값으로 값들이 전달됨
        password = request.POST.get('password') #html로부터 name 값으로 값들이 전달됨
        re_password = request.POST.get('re_password') #html로부터 name 값으로 값들이 전달됨

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            fcuser = Fcuser( #객체를 만들고
                username = username,
                password = password
            )

            fcuser.save() #객체를 세이브하고 데이터베이스에 생성이 되는지

        return render(request, 'register.html') #반환하고 싶은 html을 반환 
   

