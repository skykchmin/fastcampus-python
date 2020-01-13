from django.contrib import admin
from .models import Fcuser

# Register your models here.
# admin을 개선할 때 사용하는 파일

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # 웹상에서 출력하고 싶은 필드들을 보여준다

admin.site.register(Fcuser, FcuserAdmin)