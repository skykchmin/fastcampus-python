from django.db import models

# Create your models here.

class Fcuser(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=64, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')


    def __str__(self): # 클래스를 문자열로 변환할 때, 클래스를 문자열로 변환할 때 어떻게 변환할지 하는 함수
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name='패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'

