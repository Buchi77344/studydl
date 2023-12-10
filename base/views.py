from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sessions.models import Session
from datetime import datetime
# Create your views here.
def index(request):
     current_time = datetime.now().time()
     if current_time < datetime.strptime('12:00:00','%H:%M:%S').time():
        greeting = 'Good Morning'
     elif current_time < datetime.strptime('17:00:00','%H:%M:%S').time():
        greeting = 'Good Afternoon'
     else:
        greeting = 'Good Evening'
     username =request.session.get('username',None)
     context = {
        'greeting':greeting ,
        'username':username
     }
    
     return render (request,'index.html',context)


def register(request):
     if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save()
                request.session['username'] = user.username
                return redirect('index')
        messages.error(request, 'Password Not Thesame')
        return redirect('register')
     else:
        return render (request, 'register.html')
    

def login(request):
    return render (request, 'login.html')
    

    




  