from django.core import serializers
from django.http import HttpResponse
from test_app.models import Question


def test(request):
    question_list = Question.objects.all()
    data = serializers.serialize("json", question_list)
    print("print " + data)
    # data = Question.objects.get(id=2)
    return HttpResponse(data)
