from django.shortcuts import redirect, render
from .models import *
from .forms import *
from datetime import date

#blog section
def home(request):
    return render(request,"home.html")
#done with the blog

#Courses section
def courses(request):
    cours = Course.objects.all()
    CourseForm = CoursesFrom()
    
    if request.method == "POST":
        form = CoursesFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/courses/')

    dict={
        'cours':cours ,
        'CourseForm' : CourseForm
    }
    return render(request,'courses.html',dict)

def findCour(request , id):
    cour = Course.objects.get(id=id)
    dict={
        'cour':cour
    }
    return render(request,'cour.html',dict)

def setasdone(request , id ):
    course = Course.objects.get(id=id)
    course.done = True
    course.save()
    return redirect('/courses/')

def plannedcourses(request):
    cours = Course.objects.filter(done=False)
    dict ={
        'cours':cours ,
    }
    return render(request,'courses.html',dict)

def donecourses(request):
    cours = Course.objects.filter(done=True)
    dict ={
        'cours':cours
    }
    return render(request,'courses.html',dict)
#done with Courses

#to do app section
def todolist(request):
    tasks =Item.objects.all()
    today = date.today()
    taskForm = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todolist/')

    dict ={
        'tasks' : tasks ,
        'taskForm' : taskForm,
        'today' : today,
    }
    return render(request,'todoapp/todolist.html' , dict)

def updateTask(request , pk):
    task = Item.objects.get(id = pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
        return redirect('/todolist/')

    dict={
        'form' : form
    }
    return render(request , 'todoapp/updateTask.html' , dict)

def deleteTask(request , pk ):
    task = Item.objects.get(id = pk)

    if request.method == "POST":
        task.delete()
        return redirect('/todolist/')

    dict = {
        'task' : task
    }
    return render(request , 'todoapp/deleteTask.html' , dict )

def dailytasks(request):
    today = date.today()
    tasks = Item.objects.filter(date=today)
    taskForm = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/dailytasks/')

    dict = {
        'today' : today ,
        'tasks' : tasks ,
        'taskForm' : taskForm
    }
    return render(request , 'todoapp/dailytasks.html' , dict)
#done with ToDoApp