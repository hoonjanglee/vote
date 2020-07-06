import datetime
from django.db import models

from django.utils import timezone

# Create your models here.

# 클래스에 포함된 변수를 필드라고 한다.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # 문자열
    pub_date = models.DateTimeField('date published') # 날짜와 시간의 형태
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timdedelta(days=1)