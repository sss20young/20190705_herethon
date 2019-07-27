from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CHOICES= [
    ('Administration', 'Administration'),
    ('Economy', 'Economy'),
    ('Engineering', 'Engineering'),
    ('Art', 'Art'),
    ]

# Create your models here.
class Post(models.Model):
    title = models.CharField(null=True,max_length=100)  #제목
    belong = models.CharField(null=True,max_length=100) #소속
    about = models.TextField(null=True,blank=True) #설문조사 설명
    kind = models.CharField(max_length=100, choices=CHOICES, default='Administration') #카테고리
    URL = models.CharField(null=True,max_length=200)  #URL 주소
    date = models.DateTimeField(auto_now_add = True) # 작성 날짜
    user = models.ForeignKey(User, null=True, on_delete=False)
    
    def __str__(self):
        return self.title
    
    