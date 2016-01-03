from django.contrib import admin

from .models import Question, Answer

admin.AdminSite.site_header = "Putz Superlatives"


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    fields = (('quest_text', 'quest_sub'), 'quest_time',)
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    fields = (('ans_quest', 'ans_text', 'ans_sub'), 'ans_time',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
