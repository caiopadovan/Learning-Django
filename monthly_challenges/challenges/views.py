from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls      import reverse

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
    "december":  "We are in December, go travel"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


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
        response_data  = f"<h1>{challenge_text}</h1>"

        return HttpResponse(response_data)
    
    except:
        return HttpResponseNotFound("<h1>This Month is not suported</h1>")