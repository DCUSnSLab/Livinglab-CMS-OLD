from django.shortcuts import render, redirect
from .forms import ContentsUploadForm, ContentsDescriptionForm, SelectThemeForm
from .models import Contents, Contents_Description, Theme, User
from django.db.models import Q

def contents(request):
    print(request.user.id)

    return render(request, 'contents/contents.html')

def UploadView(request):
    print("You are in ContentUploadView")

    theme_list = Theme.objects.all()

    if request.method == 'POST':
        contentsUploadForm = ContentsUploadForm(request.POST, request.FILES)
        contentsDescriptionForm = ContentsDescriptionForm(request.POST)

        # input value 확인
        # print("contentsUploadForm:", contentsUploadForm)
        # print("contentsDescriptionForm:", contentsDescriptionForm)

        if contentsUploadForm.is_valid() and contentsDescriptionForm.is_valid():

            request_theme = request.POST['Theme']
            # theme_id = Theme.objects.get(themeValue=request_theme).id
            theme_obj = Theme.objects.get(themeValue=request_theme)

            contents = contentsUploadForm.save(commit=False)
            contents.userFK = request.user
            contents.theme_id = theme_obj
            contents.save()

            description = contentsDescriptionForm.save(commit=False)
            current_content = Contents.objects.filter(Q(userFK=request.user)).latest('id')

            description.contentFK = current_content
            description.save()

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
# TODO 특정 콘텐츠를 선택하면 해당 콘텐츠에 기존에 저장된 정보를 수정한다.(파일명, 파일, 콘텐츠 설명 등등)
# TODO 먼저 기존에 저장되어있는 정보를 들을 출력하고 각 항목 아래에 수정할 수 있는 필드를 생성한다.
def UpdateView(request, id):
    print("You are in ContentUpdate, Contents ID is %d " % id)

    contents = Contents.objects.get(id=id)
    description = Contents_Description.objects.get(contentFK=contents)
    theme_list = Theme.objects.all()

    c = Contents.objects.filter(id=id).values("theme_id")
    contents_in_theme = Theme.objects.get(id__in=c)
    contents_in_themeValue = contents_in_theme.themeValue

    # 불러온 필드 아래 값을 수정할 수 있는 별도 필드 구성
    # 수정, 취소 버튼 구성
    # 콘텐츠 삭제기능

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