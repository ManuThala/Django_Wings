from django.shortcuts import render;
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect;
from django.urls import reverse

monthly_challenges={
    'january':'Work for january',
    'february':'Work for february',
    'march':'Work for March',
    'april':'Work for April',
    'may':'Work for May',
    'june':'Work for June',
    'july':'Work for July',
    'august':'Work for August',
    'september':'Work for September',
    'october':'Work for October',
    'november':'Work for November',
    'december':'Work for December'
}

def index(request):
    list_months='';
    months=list(monthly_challenges.keys());
    for month in months:
        month_cap=month.capitalize();
        month_path=reverse('monthly-challenge',args=[month])
        list_months+=f'<li><a href=\'{month_path}\'>{month_cap}</a></li>' 
    response_data=f'<ul>{list_months}</ul>'
    return HttpResponse(response_data);
    




# create views here
def monthly_challenge_number(request,month):
    months=list(monthly_challenges.keys());

    if month < 1 or month > len(months):
        return HttpResponseNotFound('Invalid month');

    forward_month=months[month-1]
    redirect_path=reverse('monthly-challenge',args=[forward_month])   
    return HttpResponseRedirect(redirect_path);

def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        response_data=f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data);
    except:
        return HttpResponseNotFound('Invalid month')
    