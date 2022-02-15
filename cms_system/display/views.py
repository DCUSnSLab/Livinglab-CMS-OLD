from django.shortcuts import render, redirect
from contents.models import Contents, Contents_Description, Theme
import json
from django.core.serializers.json import DjangoJSONEncoder
from user.models import CustomUser

def just(request):
    print("just")

    return render(request, 'display/just.html')

def signageView(request):

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

    return render(request, 'display/signageShow.html', context)

def picDetail(request, id):
    # print("You are in ContentUpdate, Contents ID is %d. and Contents all object %s " %(id, contents))
    # user_img2 =
    # user_list = list(CustomUser.objects.all().values('user_profile'))
    contents = Contents.objects.get(id=id)
    cont_user_id = Contents.objects.filter(id=id).values("userFK")
    description_user = CustomUser.objects.filter(user__in=cont_user_id).values('user_description')
    user_img = CustomUser.objects.filter(user__in=cont_user_id).values('user_profile')
    # print("You are in ContentUpdate, Contents ID is %d. and all object '%s' and 저작자 %s 저작자 정보 %s"
    #       % (id, contents, cont_user_id, description_user))
    print(" %s 저작자 %s 저작자 정보 %s 사진 정보 %s" % (contents, cont_user_id, description_user, user_img))

    # cont_user_id = Contents.objects.get(id=id)
    # description2 = CustomUser.objects.filter(id=cont_user_id).values("user_description")
    # description2 = CustomUser.objects.get(id=id).value("user_description")
    # description2 = CustomUser.objects.first().value("user")

    description = Contents_Description.objects.get(contentFK=contents)
    theme_list = Theme.objects.all()
    # print(" %s 저작자 %s 저작자 정보 %s" % (description, cont_user_id, description_user))


    c = Contents.objects.filter(id=id).values("theme_id")
    contents_in_theme = Theme.objects.get(id__in=c)
    contents_in_themeValue = contents_in_theme.themeValue

    content2server = list(Contents.objects.filter(id=id).values('id', 'title', 'upload_file'))
    # print("content2server", content2server)

    context = {
        "contents_info": contents,
        "description_info": description,
        'theme_list': theme_list,
        'contents_in_themeValue': contents_in_themeValue,
        'description_user': description_user,
        'content2server': content2server,
        'user_img': user_img,
        # 'user_list': user_list,
    }

    return render(request, 'display/picdetail.html', context)

def mediDetail(request, id):
    # print("You are in ContentUpdate, Contents ID is %d. and Contents all object %s " %(id, contents))
    # user_img2 =
    # user_list = list(CustomUser.objects.all().values('user_profile'))
    contents = Contents.objects.get(id=id)
    cont_user_id = Contents.objects.filter(id=id).values("userFK")
    description_user = CustomUser.objects.filter(user__in=cont_user_id).values('user_description')
    user_img = CustomUser.objects.filter(user__in=cont_user_id).values('user_profile')
    # print("You are in ContentUpdate, Contents ID is %d. and all object '%s' and 저작자 %s 저작자 정보 %s"
    #       % (id, contents, cont_user_id, description_user))
    print(" %s 저작자 %s 저작자 정보 %s 사진 정보 %s" % (contents, cont_user_id, description_user, user_img))

    # cont_user_id = Contents.objects.get(id=id)
    # description2 = CustomUser.objects.filter(id=cont_user_id).values("user_description")
    # description2 = CustomUser.objects.get(id=id).value("user_description")
    # description2 = CustomUser.objects.first().value("user")

    description = Contents_Description.objects.get(contentFK=contents)
    theme_list = Theme.objects.all()
    # print(" %s 저작자 %s 저작자 정보 %s" % (description, cont_user_id, description_user))


    c = Contents.objects.filter(id=id).values("theme_id")
    contents_in_theme = Theme.objects.get(id__in=c)
    contents_in_themeValue = contents_in_theme.themeValue

    content2server = list(Contents.objects.filter(id=id).values('id', 'title', 'upload_file'))
    # print("content2server", content2server)

    context = {
        "contents_info": contents,
        "description_info": description,
        'theme_list': theme_list,
        'contents_in_themeValue': contents_in_themeValue,
        'description_user': description_user,
        'content2server': content2server,
        'user_img': user_img,
        # 'user_list': user_list,
    }

    return render(request, 'display/mediadetail.html', context)