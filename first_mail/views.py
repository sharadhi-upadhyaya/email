from django.shortcuts import render
from django.http import HttpResponse
from first_mail.simplemail import samplemail

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Email Page")

def login(request):
    return render(request, "first_mail/login.html")

def create(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
    context = {'uname': user, 'password' : pwd}
 
    # return HttpResponse("Logged in as: " +user+"/"+user)
    return render(request, 'first_mail/message.html', context)

def message(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        rcv = request.POST.get('receiver_email')
    context = {'message': msg}
    print(context)    
    response =  HttpResponse("Success")
    response_a = samplemail(msg, rcv)
    return response
    