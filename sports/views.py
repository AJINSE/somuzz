from django.shortcuts import render, redirect
from .models import sports
from .models import match, readmore
from .models import cricket, comment
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.db.models import Q
from project2.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# firstmatch = sports()
# firstmatch.date = '1/12/1997'
# firstmatch.head = 'it was a good match'
# firstmatch.sub = 'fgfhagsa gfjhadvafgjshdfvns hhsgdfjbsvdcnggs sggdfnbdfsd nsgdf usgf hgfjfhsvjff'
#
# secondmatch = sports()
# secondmatch.date = '12 12 12'
# secondmatch.head = 'amazing match'
# secondmatch.sub = 'super kaliyaan mwone'
# secondmatch.img = 'peace.jpg'
#
# thirdmatch = sports()
# thirdmatch.date = '10 10 10'
# thirdmatch.head = 'shimmi hero aada hero'
# thirdmatch.sub = 'mwone ath lockaa ing por'
# thirdmatch.img = 'psyco.jpeg'
#
# fourmatch = sports()
# fourmatch.date = '12 12 1998'
# fourmatch.head = 'vamban game'
# fourmatch.sub = 'walare migacha onn'
# fourmatch.img = 'messi.jpg'
# fourmatch.img = 'ronu.jpg'
# fourmatch.img = 'vijay.jpg'

# lis = [firstmatch, secondmatch, thirdmatch, fourmatch]


def sportss(request):
    ob = sports.objects.all()
    mt = match.objects.all()
    ab = cricket.objects.all()

    return render(request, 'index.html', {'objects': ob,
                                          'mt': mt, 'ab': ab})


# def sport(request):
#   mt = match.objects.all()


# return render(request, 'index.html', {'matches': mt})


# def loop(request):
#     return render(request, 'forloop.html', {'f': lis})


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
        print(c, d, g, h)
        if (e == f):

            if (User.objects.filter(username=c).exists()):
                messages.error(request, "username already exist")
                return redirect('sports:register-page')
            elif (User.objects.filter(email=d).exists()):
                messages.error(request, "email already exist")
                return redirect('sports:register-page')
            else:
                z = User.objects.create_user(username=c, email=d, password=e, first_name=g, last_name=h)
                z.save()
                auth.login(request, z)
                return redirect('sports:home')
        else:
            messages.error(request, "password doesn't match")
            return redirect('sports:register-page')
    return render(request, 'register.html')


def about(request):
    subject = 'Welcome to Noc Tech solutions'
    message = 'Hope you are enjoying your Django Tutorials'
    recepient = request.GET.get('comment')
    send_mail(subject,
              message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    return render(request, 'about.html', {'b': recepient})


def blog(request):
    ad = readmore.objects.order_by('-date')[0:1]
    bd = readmore.objects.order_by('date')[1:]

    return render(request, 'Blog.html', {'ad': ad, 'bd': bd})


def team(request):
    return render(request, 'team.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def search(request):
    a = request.GET.get('f', None)
    results = sports.objects.filter(Q(head__icontains=a) | Q(sub__icontains=a))
    result = match.objects.filter(Q(team1__icontains=a) | Q(team2__icontains=a))
    return render(request, 'searchresult.html', {'search': results, 'search': result})


def singleblog(request, id):
    cd = readmore.objects.get(id=id)
    return render(request, 'single-blog.html', {'cd': cd})


def botton(request):
    return render(request, 'botton.html')


def contactbox(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    address = request.POST.get('address', None)
    message = request.POST.get('message', None)
    print(name, email, address, message)
    comment.objects.create(name=name, email=email, address=address, message=message)
    return render(request, 'contactbox.html')
