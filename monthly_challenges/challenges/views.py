from django.shortcuts import render
from django.http      import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls      import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january":   "We are in January, run 10 minutes every day",
    "february":  "We are in February, eat fruit every day",
    "march":     "We are in March, practice a new sport",
    "april":     "We are in April, study another language",
    "may":       "We are in May, learn one instrument",
    "june":      "We are in June, go to the gym every day",
    "july":      "We are in July, eat less meal",
    "august":    "We are in August, study more about coding",
    "september": "We are in September, go play soccer",
    "october":   "We are in Ocotber, walk 30 minutes every day",
    "november":  "We are in November, learn how to cook",
    "december":   None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path  =  reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    
    except:
        raise Http404()