from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import Todo_db
from .forms import TODOForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.decorators import login_required


@login_required(login_url='login_user')
def addtodo(request):

    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = Todo_db.objects.filter(user=user)
        
        return render(request,'addtodo.html',context={'form':form,'todos':todos})
def index(request):
    return render(request,'index.html')
def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context ={'form':form}
        return render(request,'login_user.html',context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return redirect('addtodo')
           return
        else:
            context = {'form':form}
            return render(request,'login_user.html',context=context)

def signup_user(request):
     if request.method == 'GET':
        form = UserCreationForm()
        context ={
            "form":form
            }
        return render(request,'signup_user.html',context=context)
     else:
        
        form = UserCreationForm(request.POST)
        context ={
            "form":form
            }
        if form.is_valid():
           user = form.save()
           if user is not None:
               return redirect('login_user')
        else:
            return render(request,'signup_user.html',context=context)

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user

        form = TODOForm(request.POST)
        if form.is_valid():
            todos = form.save(commit=False)
            todos.user = user
            todos.save()

            return redirect("addtodo")
        else:
            return render(request,'signup_user.html')
     
def logout_user(request):
    logout(request)
def delete(request,id):
    Todo_db.objects.get(pk=id).delete()
    return redirect('addtodo')

def complete_todo(request,id):
    todo = Todo_db.objects.get(pk=id)
    todo.completed = True
    todo.save()
    return redirect('addtodo')









