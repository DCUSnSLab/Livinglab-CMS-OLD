from django.shortcuts import render
from contents.models import Contents
import json
from django.core.serializers.json import DjangoJSONEncoder

def just(request):
    print("just")

    return render(request, 'display/just.html')

def signageView(request):

    # For Gallery Show
    contents_list = list(Contents.objects.all().values('id', 'title', 'upload_file'))
    print("For Gallery Show")
    print("contents_list : \n", contents_list)
    print("type : ", type(contents_list))
    print()

    # objects.all + values() + list() + specific field
    # contents_object_val_list_spec = list(Contents.objects.all().values('id', 'title', 'upload_file'))
    # print("objects.all + values() list() + specific field")
    # print("contents_object_val_list_spec : \n", contents_object_val_list_spec)
    # print("type : ", type(contents_object_val_list_spec))
    # print()

   # Django Json Encoder
    contents_serach = Contents.objects.all().values()
    contents_list_dic = json.dumps(list(contents_serach), cls=DjangoJSONEncoder)
    print("Django Json Encoder")
    print("contents_list_json : \n", contents_list_dic)
    print("type : ", type(contents_list_dic))
    print()

    # django 오브젝트를 다양하게 출력하는 방법

    # # objects.all + list() + values()
    # contents_object_val_list = list(Contents.objects.all().values())
    # print("objects.all + list() + values()")
    # print("contents_object_val_list : \n", contents_object_val_list)
    # print("type : ", type(contents_object_val_list))
    # print()

    # # For Spotlight Show
    # # objects.all
    # contents_object = Contents.objects.all()
    # print("objects.all")
    # print("contents_object : \n", contents_object)
    # print()
    #
    # # objects.all + list()
    # contents_object_list = list(Contents.objects.all())
    # print("objects.all + list()")
    # print("contents_object_list : \n", contents_object_list)
    # print()
    #
    # # objects.all + values()
    # contents_object_val = Contents.objects.all().values()
    # print("objects.all + values()")
    # print("contents_object_val : \n", contents_object_val)
    # print()
    # # objects.all + values() + specific field
    # contents_object_val_spec = Contents.objects.all().values('id', 'title', 'upload_file')
    # print("objects.all + values() + specific field")
    # print("contents_object_val_spec : \n", contents_object_val_spec)
    # print()
    # # objects.all + values_list()
    # contents_object_vallist = Contents.objects.all().values_list()
    # print("objects.all + values_list()")
    # print("contents_object_vallist : \n", contents_object_vallist)
    # print()
    #
    # # objects.all + list() + values_list()
    # contents_object_vallist_list = list(Contents.objects.all().values_list())
    # print("objects.all + list() + values_list()")
    # print("contents_object_vallist_list : \n", contents_object_vallist_list)
    # print()

    context = {
        "contents_list": contents_list,
        # "contents_object_val_list_spec": contents_object_val_list_spec,
        "contents_list_dic": contents_list_dic,
    }

    return render(request, 'display/signageShow.html', context)

def projectorView(request):

    data  = None
    testVale  = Contents.objects.all()
    if request.method == 'POST':

        data = json.loads(request.body)
        print("data : ", data['upload_file'])

        context = {
            "projector_content": data,
        }
        print("context : ", context)
        return render(request, 'display/projectorShow.html', context)

    else:
        context = {
            "projector_content": testVale,
        }

        print("context : ", context)
        return render(request, 'display/projectorShow.html', context)










def testView(request):
    # For Gallery Show
    contents_list = list(Contents.objects.all().values('id', 'title', 'upload_file'))
    print("For Gallery Show")
    print("contents_list : \n", contents_list)
    print("type : ", type(contents_list))
    print()

    # Django Json Encoder
    contents_serach = Contents.objects.all().values()
    contents_list_dic = json.dumps(list(contents_serach), cls=DjangoJSONEncoder)
    print("Django Json Encoder")
    print("contents_list_json : \n", contents_list_dic)
    print("type : ", type(contents_list_dic))
    print()

    context = {
        "contents_list": contents_list,

        "contents_list_dic": contents_list_dic,
    }

    return render(request, 'display/test.html', context)

def test2(request):
    pass
    return render(request, 'display/test2.html')

def test3(request):
    contents_list = Contents.objects.all()

    print("c : ", contents_list)

    context = {"contents_list": contents_list}
    return render(request, 'display/test3.html', context)