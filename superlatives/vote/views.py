from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from models import Question, Answer
from putz import Putzen

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
    Submit a response
    """
    if request.method == "POST":

        for quest in request.POST:

            if quest != "csrfmiddlewaretoken":

                # Get answer to form
                ans = request.POST[quest]

                if ans:
                    # TODO: Allow input of a list of names
                    # Filter the response
                    filtered_ans = ans.lower().strip()

                    # Map to putzen kerberos
                    try:
                        putzen = Putzen(filtered_ans).name
                    except KeyError:
                        putzen = ans

                    # Try to increment previous answer
                    try:
                        # Get previous answer
                        prev_answer = Answer.objects.filter(
                            ans_text=putzen
                        ).get(
                            ans_quest__quest_text=quest
                        )

                        # Incremement the counter
                        prev_answer.ans_count += 1

                        # Save the model to database
                        prev_answer.save()

                    except Answer.DoesNotExist:
                        # If you can't then create a new answer object
                        # Make new answer object
                        a = Answer()

                        # TODO: Save the submitter
                        a.ans_sub = "admin"

                        a.ans_count = 1

                        a.ans_text = putzen

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
