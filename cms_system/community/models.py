from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Community(models.Model):
    id = models.AutoField(primary_key=True)  # 게시판id
    name = models.CharField(max_length=50)  # 게시판제목
    createDate = models.DateTimeField(auto_now_add=True)  # 게시판생성시간
    # Category_id

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)  # 게시글id
    title = models.TextField()  # 게시글제목
    # viewcount = models.PositiveIntegerField(default=0)  # 조회수
    content = HTMLField()  # 게시글내용
    createDate = models.DateTimeField(auto_now_add=True)  # 게시글작성시간
    lastEditDate = models.DateTimeField(auto_now_add=True)  # 게시글수정시간
    Community_id = models.ForeignKey(Community, default=1, on_delete=models.CASCADE)  # 게시판
    # auth_user_id

    # postname이 postobject 대신
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)  # 댓글id
    content = models.TextField()  # 댓글내용
    createDate = models.DateTimeField(auto_now_add=True)  # 댓글작성시간
    lastEditDate = models.DateTimeField(auto_now_add=True)  # 댓글수정시간
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)  # 게시글
    # auth_user_id

    def __str__(self):
        return self.content
