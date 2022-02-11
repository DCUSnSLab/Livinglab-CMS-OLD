from django.shortcuts import render

def index(request):
    print("현재 계정 {0} 현재 계정 ID {1}".format(request.user, request.user.id))

    return render(request, 'index.html')
