from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'    
        }, 
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'    
        },
        widget=forms.PasswordInput, label="비밀번호") 
    # 비밀번호 가리기

    def clean(self):
        cleaned_data = super().clean() #super를 통해 기존에 있던 clean함수를 호출 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else: #self를 통해 class변수로 들어간다
                self.user_id = fcuser.id #id를 가져오는 것 