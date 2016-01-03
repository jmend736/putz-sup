from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


# Submitter Model
class Submitter(models.Model):
    sub_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.sub_name


# Question Model
class Question(models.Model):

    quest_text = models.CharField(max_length=200)
    quest_sub = models.ManyToManyField(Submitter)
    quest_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.quest_text


# Answer Model
class Answer(models.Model):
    ans_text = models.CharField(max_length=200)
    ans_quest = models.ForeignKey(Question)
    ans_sub = models.ManyToManyField(Submitter)
    ans_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.ans_text
