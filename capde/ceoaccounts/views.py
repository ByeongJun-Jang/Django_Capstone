from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
import capde.views

def ceo_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None) 
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        
        err_data={}
        if not(username and useremail and password and re_password):
            err_data['error'] = '모든 값을 입력해주세요.'
        
        elif password != re_password:
            err_data['error'] = '비밀번호가 다릅니다.'
        
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password),
            )
            user.save()

        return render(request, 'register.html', err_data)

def ceo_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('ceo_main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        return redirect('capde:ceo_main')#render(request,'index/test.html',{'user':user})
    else:
        return HttpResponse("로그인 해주세요!")

def logout(request):
    pass