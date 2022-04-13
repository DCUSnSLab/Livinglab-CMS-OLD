import base64
import io
import pickle

import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib as plt

import os.path
import random
from datetime import time, datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage, FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Community, Post, Comment, Board
from django.core.paginator import Paginator
import json
from django.views.decorators.csrf import csrf_exempt

import base64
from PIL import Image


# Create your views here.
# 게시판 리스트
def index(request):
    communitylist = Community.objects.all()
    return render(request, 'communityapp/index.html', {'communitylist': communitylist})


# 게시글 리스트
def community(request, id):
    community = get_object_or_404(Community, id=id)
    postlist = Post.objects.filter(Community_id=community.id).order_by('-createDate')
    page = request.GET.get('page', '1')
    paginator = Paginator(postlist, 20)
    page_obj = paginator.page(page)
    context = {
        'community': community,
        'post_list': postlist,
        'page_obj': page_obj,
    }
    return render(request, 'communityapp/blog.html', context)


# 게시글
def posting(request, id, pk):
    community = get_object_or_404(Community, id=id)
    # 게시글 중에서 pk(primary_key)를 이용해 하나의 게시글 검색
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(Post_id=post.id)
    replycomment = list(Comment.objects.filter(id=id).values('id', 'content', 'parent_comment'))
    post.save()
    context = {
        'community': community,
        'post': post,
        'comment': comment,
        'replycomment': replycomment,
    }
    return render(request, 'communityapp/posting.html', context)


# 게시글 작성
def new_post(request, id):
    community = get_object_or_404(Community, id=id)
    if request.method == 'POST':
        post = Post()
        post.Community_id = get_object_or_404(Community, id=id)
        post.title = request.POST['postname']
        post.content = request.POST['contents']
        post.createDate = timezone.datetime.now()
        post.lastEditDate = timezone.datetime.now()
        post.userFK = request.user
        post.save()
        return redirect('community', id)
    context = {
        'community': community,
    }
    return render(request, 'communityapp/newpost.html', context)


# 게시글 수정
def edit_post(request, id, pk):
    community = get_object_or_404(Community, id=id)
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.Community_id = get_object_or_404(Community, id=id)
        post.title = request.POST['postname']
        post.content = request.POST['contents']
        post.lastEditDate = timezone.datetime.now()
        post.save()
        return redirect('posting', id, pk)
    context = {
        'community': community,
        'post': post,
    }
    return render(request, 'communityapp/editpost.html', context)


# 게시글 삭제
def remove_post(request, id, pk):
    community = get_object_or_404(Community, id=id)
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('community', id)
    context = {
        'community': community,
        'post': post,
    }
    return render(request, 'communityapp/removepost.html', context)


# 댓글 작성
def reply(request, id, pk):
    community = get_object_or_404(Community, id=id)
    if request.method == "POST":
        comment = Comment()
        comment.Post_id = Post.objects.get(pk=pk)
        comment.content = request.POST['comment']
        comment.createDate = timezone.datetime.now()
        comment.lastEditDate = timezone.datetime.now()
        comment.userFK = request.user
        comment.save()
        return redirect('posting', id, pk)
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(id=post.id)
    post.save()
    context = {
        'community': community,
        'post': post,
        'comment': comment,
    }
    return render(request, 'communityapp/posting.html', context)


# 대댓글 작성
def rereply(request, id, pk, rid):
    community = get_object_or_404(Community, id=id)
    if request.method == "POST":
        comment = Comment()
        comment.Post_id = Post.objects.get(pk=pk)
        comment.content = request.POST['comment']
        comment.createDate = timezone.datetime.now()
        comment.lastEditDate = timezone.datetime.now()
        comment.parent_comment = Comment.objects.get(id=rid)
        comment.userFK = request.user
        comment.save()
        return redirect('posting', id, pk)
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(id=post.id)
    post.save()
    context = {
        'community': community,
        'post': post,
        'comment': comment,
    }
    return render(request, 'communityapp/posting.html', context)


# 댓글 수정
def edit_reply(request, id, pk, rid):
    community = get_object_or_404(Community, id=id)
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(id=rid)
    if request.method == "POST":
        comment.content = request.POST['comment']
        comment.lastEditDate = timezone.datetime.now()
        comment.save()
        return redirect('posting', id, pk)
    context = {
        'community': community,
        'post': post,
        'comment': comment,
    }
    return render(request, 'communityapp/editreply.html', context)


# 댓글 삭제
def remove_reply(request, id, pk, rid):
    community = get_object_or_404(Community, id=id)
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(id=rid)
    if request.method == 'POST':
        comment.delete()
        return redirect('posting', id, pk)
    context = {
        'community': community,
        'post': post,
        'comment': comment,
    }
    return render(request, 'communityapp/removereply.html', context)


# 그림판
def paint(request):
    return render(request, 'communityapp/paint.html')

# 웹소켓 테스트용
def test(request):
    return render(request, 'communityapp/test.html')

# 그림판 저장..?
@csrf_exempt
def paintlist(request):
    board = Board()
    getboard = Board.objects.all()
    if request.method == 'POST':
        # print(json.loads(request.body))
        requestImg = json.loads(request.body)
        byteImg = bytes(requestImg['imgBase64'], 'utf-8')
        imgDecode = base64.b64decode(byteImg)
        image = Image.open(io.BytesIO(imgDecode))
        filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
        imagePath = './media/community/drawing/{0}.png'.format(filename1)
        print(imagePath)
        image.save(imagePath, 'png')
        board.path = '.'+imagePath
        board.save()
    context = {
        'board': getboard,
    }
    return render(request, 'communityapp/paintlist.html', context)

