from django.shortcuts import render, redirect
from .forms import ContentsUploadForm, ContentsDescriptionForm
from .models import Contents, Contents_Description, Theme
from django.db.models import Q
from .files import *
from .mediaProcessing import *
from django.contrib.auth.models import User
import os

def contents(request):
    print(request.user.id)

    return render(request, 'contents/contents.html')

def UploadView(request):
    print("contents/views/UploadView")
    print("현재 계정 {0} 현재 계정 ID {1}".format(request.user, request.user.id))

    theme_list = Theme.objects.all()

    if request.method == 'POST':
        contentsUploadForm = ContentsUploadForm(request.POST, request.FILES)
        contentsDescriptionForm = ContentsDescriptionForm(request.POST)

        if contentsUploadForm.is_valid() and contentsDescriptionForm.is_valid():

            file = (str(contentsUploadForm.cleaned_data['upload_file']))
            filename, fileType = FileTypeCheck(file)


            request_theme = request.POST['Theme']
            # theme_id = Theme.objects.get(themeValue=request_theme).id
            theme_obj = Theme.objects.get(themeValue=request_theme)

            contents = contentsUploadForm.save(commit=False)
            contents.userFK = request.user
            contents.contentType = fileType
            contents.theme_id = theme_obj
            contents.save()

            description = contentsDescriptionForm.save(commit=False)
            current_content = Contents.objects.filter(Q(userFK=request.user)).latest('id')

            description.contentFK = current_content


            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            BASE_PATH = "{0}/media/contents/UID-{1}/{2}".format( \
                BASE_DIR, request.user.id, fileType)

            if fileType == "IMG":

                FILE_DIR = "{0}/vod-{1}/".format(BASE_PATH, filename)
                IMG_PATH = "{0}/{1}".format(BASE_PATH, file)
                VOD_PATH = "{0}/vod-{1}/{2}.mp4".format(BASE_PATH, filename, filename)
                TS_PATH = "{0}/vod-{1}/clip_%04d.ts".format(BASE_PATH, filename)
                M3U8_PATH = "{0}/vod-{1}/{2}.m3u8".format(BASE_PATH, filename, filename)

                createDirectory(FILE_DIR)
                vodConvert = img2video(IMG_PATH, VOD_PATH)
                video2m3u8(VOD_PATH, TS_PATH, M3U8_PATH, vodConvert)

                fileInfo = GetFileInfo(IMG_PATH, fileType)
                description.width = fileInfo['width']
                description.height = fileInfo['height']
                description.HVType = fileInfo['HVType']
                description.save()

            else:  # VOD

                FILE_DIR = "{0}/vod-{1}/".format(BASE_PATH, filename)
                VOD_PATH = "{0}/{1}.mp4".format(BASE_PATH, filename)
                TS_PATH = "{0}/vod-{1}/clip_%04d.ts".format(BASE_PATH, filename)
                M3U8_PATH = "{0}/vod-{1}/{2}.m3u8".format(BASE_PATH, filename, filename)
                THUMBNAIL_PATH = "{0}/thumbnail-{1}/".format(BASE_PATH, filename)

                createDirectory(FILE_DIR)
                video2m3u8(VOD_PATH, TS_PATH, M3U8_PATH, 0)

                fileInfo = GetFileInfo(VOD_PATH, fileType)
                description.width = fileInfo['width']
                description.height = fileInfo['height']
                description.HVType = fileInfo['HVType']
                description.save()

                # 비디오 프레임 추출
                DIR = createDirectory(THUMBNAIL_PATH)
                print("sdfdsfds", DIR)
                print(VOD_PATH)
                GetThumbnail(VOD_PATH, DIR)



        return redirect('/')
    else:
        contentsUploadForm = ContentsUploadForm()
        contentsDescriptionForm = ContentsDescriptionForm()

        context = {
            'contentsUploadForm': contentsUploadForm,
            'contentsDescriptionForm': contentsDescriptionForm,
            'theme_list': theme_list
        }
        return render(request, 'contents/contents_Upload.html', context)

# UpdateView
def UpdateView(request, id):
    print("You are in ContentUpdate, Contents ID is %d " % id)

    contents = Contents.objects.get(id=id)
    description = Contents_Description.objects.get(contentFK=contents)
    theme_list = Theme.objects.all()

    c = Contents.objects.filter(id=id).values("theme_id")
    contents_in_theme = Theme.objects.get(id__in=c)
    contents_in_themeValue = contents_in_theme.themeValue

    if request.method == 'POST':
        contentsUploadForm = ContentsUploadForm(request.POST, request.FILES)
        contentsDescriptionForm = ContentsDescriptionForm(request.POST)

        if contentsUploadForm.is_valid() and contentsDescriptionForm.is_valid():

            request_theme = request.POST['Theme']
            # theme_id = Theme.objects.get(themeValue=request_theme).id
            theme_obj = Theme.objects.get(themeValue=request_theme)

            contents.title = contentsUploadForm.cleaned_data['title']
            contents.contentType = contentsUploadForm.cleaned_data['contentType']
            contents.upload_file = contentsUploadForm.cleaned_data['upload_file']
            contents.userFK = request.user
            contents.theme_id = theme_obj
            contents.save()

            description.description = contentsDescriptionForm.cleaned_data['description']
            description.save()

        return redirect('/')
    else:
        contentsUploadForm = ContentsUploadForm()
        contentsDescriptionForm = ContentsDescriptionForm()

        context = {
            'contentsUploadForm': contentsUploadForm,
            'contentsDescriptionForm': contentsDescriptionForm,
            "contents_info": contents,
            "description_info": description,
            'theme_list': theme_list,
            'contents_in_themeValue': contents_in_themeValue
        }

    return render(request, 'contents/contents_update.html', context)

def DashboardView(request):
    print("You are in ContentDashboard")

    # 현재 사용자 ID 가지고 오기
    current_user = request.user
    current_user_id = User.objects.get(username=current_user).id
    # print("contentsID : ", current_user_id)

    # 업로드한 객체에서 사용자의 ID를 가지는 객체만 추리기
    # 해당 객체의 파일 경로 가지고 오기
    # get()는 1개의 객체, 여러개의 객체는 filter() 사용
    # value('필드명') : 해당 필드에 대해서만 추출

    contents = Contents.objects.filter(userFK=current_user_id).values('id', 'title', 'upload_file')

    context = {"contents_list": contents}
    return render(request, 'contents/contents_dashboard.html', context)


def DeleteView(request, id):

    print("You are in ContentDelete, Contents ID is %d " % id)
    print("delete!!")
    content = Contents.objects.get(id=id)
    content.delete()
    return redirect('/contents/dashboard/')

def HideView(request, id):
    pass