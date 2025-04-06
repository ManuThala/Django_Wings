from django.shortcuts import render;
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect;
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
    'december':None
}

def index(request):
    months=list(monthly_challenges.keys()); 
    return render(request,'challenges/index.html',{'months':months});
    

    
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
        # response_data=render_to_string('challenges/challenge.html')
        return render(request, 'challenges/challenge.html',{'text':challenge_text,'month_name':month});
    except:
        raise Http404('This month is not supported!');
    