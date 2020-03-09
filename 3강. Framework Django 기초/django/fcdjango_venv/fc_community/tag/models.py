from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') # 기존에 있던 meta데이터를 복사


    def __str__(self): # 클래스를 문자열로 변환할 때, 클래스를 문자열로 변환할 때 어떻게 변환할지 하는 함수
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name='패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'