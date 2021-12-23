from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("selected_choice", selected_choice)

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        # 선택 횟수를 늘리면 코드는 일반 HttpResponse가 아닌 HttpResponseRedirect를 반환합니다.
        # HttpResponseRedirect는 사용자가 리디렉션될 URL이라는 단일 인수를 사용합니다
        # (이 경우 URL을 구성하는 방법은 다음 항목 참조)
    # 위의 Python 주석이 지적했듯이 POST 데이터를 성공적으로 처리한 후에는 항상 HttpResponseRedirect를 반환해야 합니다.
    # 이 예제에서는 HttpResponseRedirect 생성자에서 reverse() 함수를 사용하고 있습니다.
    # 이 기능을 사용하면 보기 기능에서 URL을 하드코딩하지 않아도 됩니다.
    # 제어를 전달하려는 뷰의 이름과 해당 뷰를 가리키는 URL 패턴의 변수 부분이 제공됩니다.
    # 이 경우 자습서 3에서 설정한 URLconf를 사용하여 이 reverse() 호출은 다음과 같은 문자열을 반환합니다.