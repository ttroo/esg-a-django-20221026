from pyexpat import model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)  # 길이 제한 가능
    content = models.TextField()             # 길이 제한 불가


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정


    def __str__(self):
        return f'[{self.pk}]{self.title}'
        
        # f'{}' <- {}안에 들어있는 걸 str 형태로 바꿔줌!
        # 따옴표 안에 있는 모든 내용은 이미 문자임!
        # int + str 불가능하니까 int를 str로 바꿔주는 방법임!