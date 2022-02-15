from django.shortcuts import render
from contents.models import Contents, Contents_Description, Theme
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    # For Gallery Show
    contents_list = list(Contents.objects.all().values('id', 'title', 'upload_file'))

    # 이예지 추가 필요
    # print contents_list
    # [1번 콘텐츠 id, title, uploadfile, userfk, themea ] [2번 ] [3] [4]
    # for
    # seraching contents_list
    # userFK, find username of userFK in User model, put this username into list

    # 아직안만들었음
    img_list = list(Contents.objects.filter(contentType='IMG'))
    vod_list = list(Contents.objects.filter(contentType='VOD'))

    print("img", img_list)
    print("vod", vod_list)

    # Django Json Encoder
    contents_serach = Contents.objects.all().values()
    contents_list_dic = json.dumps(list(contents_serach), cls=DjangoJSONEncoder)

    context = {
        "contents_list": contents_list,
        "img_list": img_list,
        "vod_list": vod_list,
        # "contents_object_val_list_spec": contents_object_val_list_spec,
        "contents_list_dic": contents_list_dic,
    }
    print("현재 계정 {0} 현재 계정 ID {1}".format(request.user, request.user.id))

    return render(request, 'index.html', context)
