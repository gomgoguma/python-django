from django.http import HttpResponse


def test(request):
    return HttpResponse("안녕하세요.")
