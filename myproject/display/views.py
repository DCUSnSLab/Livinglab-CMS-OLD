from django.shortcuts import render
from contents.models import Contents

def just(request):
    print("just")

    return render(request, 'display/just.html')

def signageView(request):

    contents_list = Contents.objects.all()

    print("c : ", contents_list)

    context = {"contents_list": contents_list}

    return render(request, 'display/signageShow.html', context)
    # return render(request, 'display/fullpage.html', context)

def testView(request):

    contents_list = Contents.objects.all()

    print("c : ", contents_list)

    context = {"contents_list": contents_list}

    return render(request, 'display/test.html', context)

def test2(request):
    pass
    return render(request, 'display/test2.html')

def test3(request):
    contents_list = Contents.objects.all()

    print("c : ", contents_list)

    context = {"contents_list": contents_list}
    return render(request, 'display/test3.html', context)