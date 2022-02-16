from django.shortcuts import render, redirect
from contents.models import Contents, Contents_Description, Theme
import json
from django.core.serializers.json import DjangoJSONEncoder
from user.models import CustomUser

def just(request):
    print("just")

    return render(request, 'display/just.html')

def signageView(request):

    img_list = Contents.objects.filter(contentType='IMG')
    vod_list = Contents.objects.filter(contentType='VOD')
    thumbnail_list = Contents_Description.objects.exclude(thumbnailPath=None).values('thumbnailPath')

    # print("img", img_list)
    # print("vod", vod_list)
    # print("thumbnail_list", thumbnail_list)

    for idx, img in enumerate(img_list):

        usernickname = CustomUser.objects.get(user_id=img.userFK_id)
        img.nickname = usernickname.nickname

    for idx, vod in enumerate(vod_list):
        # print("vod {0}".format(vod))
        vod.thumbnail = thumbnail_list[idx]['thumbnailPath']
        usernickname = CustomUser.objects.get(user_id=vod.userFK_id)
        vod.nickname = usernickname.nickname

    context = {
        "img_list": img_list,
        "vod_list": vod_list,
    }

    return render(request, 'display/signageShow.html', context)

def picDetail(request, id):

    contents = Contents.objects.get(id=id)
    cont_user_id = Contents.objects.filter(id=id).values("userFK")
    description_user = CustomUser.objects.filter(user__in=cont_user_id).values('user_description')
    user_img = CustomUser.objects.filter(user__in=cont_user_id).values('user_profile')

    description = Contents_Description.objects.get(contentFK=contents)
    theme_list = Theme.objects.all()


    c = Contents.objects.filter(id=id).values("theme_id")
    contents_in_theme = Theme.objects.get(id__in=c)
    contents_in_themeValue = contents_in_theme.themeValue

    nickname = CustomUser.objects.get(user_id=contents.userFK_id)
    contents.nickname = nickname




    content2server = list(Contents.objects.filter(id=id).values('id', 'title', 'upload_file'))

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

    nickname = CustomUser.objects.get(user_id=contents.userFK_id)
    contents.nickname = nickname

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