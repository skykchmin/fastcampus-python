from django.db import models

# Create your models here.

class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete = models.CASCADE,
    verbose_name='작성자')
    # DB로 연결 Foreignkey를 사용하는 방법 / 여러모델들을 아이디로 연결하는데  
    # Foreignkey를 이용하면 on_delete를 사용해야함 // 사용자가 삭제했을 경우, 사용자가 쓴 게시글을 지우기 위해서
    # foreignkey가 가르키고 있는 애가 삭제되면 자기 자신을 어떻게 할건지를 결정해야하는데 cascade는 사용자가 쓴 것을 전부 삭제한다
    # cascade 이외에도 null, set_default를 할 수 있다 
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')


    def __str__(self): # 클래스를 문자열로 변환할 때, 클래스를 문자열로 변환할 때 어떻게 변환할지 하는 함수
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name='패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'

