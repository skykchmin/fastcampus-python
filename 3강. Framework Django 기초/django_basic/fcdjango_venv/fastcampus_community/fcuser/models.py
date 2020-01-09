from django.db import models

# Create your models here.

class Fcuser(models.Model): #models.Model을 상속받아야한다
    usernmae = models.CharField(max_length=64, verbose_name='사용자명') #charfield(문자열)을 담을수 있는 공간 만듬
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') #auto_now_add(저장하는 시간을 넣어준다)
    