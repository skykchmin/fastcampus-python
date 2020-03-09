from django.contrib import admin
from .models import Tag
# Register your models here.

# 기존에 만들어져있던 곳에서 복사
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',) # 웹상에서 출력하고 싶은 필드들을 보여준다

admin.site.register(Tag, TagAdmin)
