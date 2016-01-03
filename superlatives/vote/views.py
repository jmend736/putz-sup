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
    return HttpResponse("This is the index page.")


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
    return HttpResponse("This page submits a question")


def submit(request):
    """
    Submit a question
    """
    if request.method == "POST":

        for quest in request.POST:

            # Get answer to form
            ans = request.POST[quest]

            # Make new answer object
            q = Answer()
            q.ans_text = ans

            # TODO: Save the submitter
            # q.ans_sub = ????

            if quest != "csrfmiddlewaretoken":

                # Update the Answers to Seleted Questions
                i = Question.objects.get(quest_text=quest)

                # Set the ForeignKey
                q.ans_quest = i

                # Write to database
                q.save()

        return HttpResponseRedirect('/vote/list/')
    else:
        # TODO: Make this page
        return HttpResponse("You stumbled across the wrong page!")


def responses(request):
    """
    Submit a question
    """
    return HttpResponse("This page shows all the responses")
