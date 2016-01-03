from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


# Submitter Model (DEPRECIATED)
# class Submitter(models.Model):
    # sub_name = models.CharField(max_length=30)

    # def __unicode__(self):
        # return self.sub_name

# Question Model
class Question(models.Model):

    quest_text = models.CharField("Question Text", max_length=200)
    quest_sub = models.CharField("Submitter", max_length=30,
                                 default="admin")
    quest_time = models.DateTimeField("Submitted On", default=timezone.now)

    def answers(self):
        return Answer.objects.filter(ans_quest=self)

    def __unicode__(self):
        return self.quest_text


# Answer Model
class Answer(models.Model):
    ans_text = models.CharField(max_length=200)
    ans_quest = models.ForeignKey(Question, null=True)
    ans_sub = models.CharField("Submitter", max_length=30,
                               default="admin")
    ans_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.ans_text
