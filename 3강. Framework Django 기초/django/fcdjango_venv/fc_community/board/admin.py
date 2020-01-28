from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',) # 웹상에서 출력하고 싶은 필드들을 보여준다

admin.site.register(Board, BoardAdmin)