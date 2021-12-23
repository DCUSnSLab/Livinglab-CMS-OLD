from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import UserAdditionalSignUpForm, UserSignUpForm
from .models import CustomUser




# 회원 가입
def just(request):
    print("just")

    return render(request, 'user/justpage.html')

def signup(request):
    if request.method == 'POST':

        form = UserSignUpForm(request.POST)
        additional_form = UserAdditionalSignUpForm(request.POST, request.FILES)


        if form.is_valid() and additional_form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = form.save()

            customuser = additional_form.save(commit=False) # 지금 저장하지 않겠다.
            customuser.user = user
            customuser.save()
            user = authenticate(username=username, password=password)

            return redirect('/')
    else:
        form = UserSignUpForm()
        additional_form = UserAdditionalSignUpForm()

    context = {'form': form, 'additional_form': additional_form}
    return render(request, 'user/signup.html', context)

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인, 현재 계정 명 확인
            auth.login(request, user)

            print("login success")
            print("current user " + str(user))
            return redirect('/')        # 203.250.33.53 으로 직행
    # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            error_msg = 'username or password is incorrect.'
            return render(request, 'user/login.html', {'error': error_msg})

    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'user/login.html')


# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    auth.logout(request)
    return redirect('/')