from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)  # 길이가 있는 문자열
    content = models.TextField()  # 길이가 없는 문자열
    create_date = models.DateTimeField()  # 날짜 시간

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 외래키, 연쇄 삭제
    content = models.TextField()
    create_date = models.DateTimeField()


class Test(models.Model):
    name = models.TextField()
