from django.shortcuts import render, redirect
from .models import sports
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse

firstmatch = sports()
firstmatch.date = '1/12/1997'
firstmatch.head = 'it was a good match'
firstmatch.sub = 'fgfhagsa gfjhadvafgjshdfvns hhsgdfjbsvdcnggs sggdfnbdfsd nsgdf usgf hgfjfhsvjff'

secondmatch = sports()
secondmatch.date = '12 12 12'
secondmatch.head = 'amazing match'
secondmatch.sub = 'super kaliyaan mwone'
secondmatch.img = 'peace.jpg'

thirdmatch = sports()
thirdmatch.date = '10 10 10'
thirdmatch.head = 'shimmi hero aada hero'
thirdmatch.sub = 'mwone ath lockaa ing por'
thirdmatch.img = 'psyco.jpeg'

fourmatch = sports()
fourmatch.date = '12 12 1998'
fourmatch.head = 'vamban game'
fourmatch.sub = 'walare migacha onn'
fourmatch.img = 'messi.jpg'
fourmatch.img = 'ronu.jpg'
fourmatch.img = 'vijay.jpg'

lis = [firstmatch, secondmatch, thirdmatch, fourmatch]


def sportss(request):
    return render(request, 'index.html', {'fm': firstmatch, 'sm': secondmatch, 'tm': thirdmatch})


def loop(request):
    return render(request, 'forloop.html', {'f': lis})


def jaya(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['password']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('sports:home')
        else:
            messages.error(request, "invalid username/password")

    return render(request, 'login.html')

def out(request):
    auth.logout(request)
    return redirect('sports:home')


def reg(request):

    if request.method == 'POST':
        c = request.POST['fullname']
        d = request.POST['youremail']
        e = request.POST['password']
        f = request.POST['confirm-password']
        g = request.POST['firstname']
        h = request.POST['lastname']
        print(c,d,g,h)
        z = User.objects.create_user(username=c,email=d,password=e,first_name=g,last_name=h)
        z.save()
    return render(request, 'register.html')