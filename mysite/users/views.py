from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """注册新用户"""
    if request.method != 'POST':
       form = UserCreationForm()
    else:
       # 处理填写的注册表单
       form = UserCreationForm(data=request.POST)
       if form.is_valid():
           new_user = form.save()
           #让用户自己登录，再重定向到主页
           authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
           login(request,authenticated_user)
           return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)


