from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    Question = models.ForeignKey(
        Question, on_delete=models.CASCADE)  # Foreign key de question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
