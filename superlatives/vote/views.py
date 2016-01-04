from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from models import Question, Answer

# Create your views here.


def index(request):
    """
    Show the number of Votes
    Show the number of questions
    Show the number of visits
    # Show the current number of people on the site
    """
    return render(request, "vote/index.html", )


def questions(request):
    """
    Show a list of the questions
    Allow people to respond here
    """
    question_list = Question.objects.all()
    context = {
        'question_list': question_list,
    }
    return render(request, 'vote/questions.html', context)


def submit_question(request):
    """
    Show a list of the questions
    Allow people to respond here
    """
    if request.method == "POST":
        new_question = request.POST['new_quest']
        q = Question()
        q.quest_text = new_question

        # TODO: Set the submitter
        q.quest_sub = "admin"

        q.save()

        return HttpResponseRedirect("/vote/")
    else:
        return render(request, "vote/newquest.html",)


def submit(request):
    """
    Submit a question
    """
    if request.method == "POST":

        for quest in request.POST:

            # Get answer to form
            ans = request.POST[quest]

            # Make new answer object
            a = Answer()
            a.ans_text = ans

            # TODO: Save the submitter
            a.ans_sub = "admin"

            if quest != "csrfmiddlewaretoken":

                # Update the Answers to Seleted Questions
                i = Question.objects.get(quest_text=quest)

                # Set the ForeignKey
                a.ans_quest = i

                # Write to database

                a.save()

        return HttpResponseRedirect('/vote/list/')
    else:
        # TODO: Make this page
        return HttpResponse("You stumbled across the wrong page!")


def responses(request):
    """
    Submit a question
    """

    context = {
        'all_questions': Question.objects.all(),
    }
    return render(request, "vote/responses.html", context)
