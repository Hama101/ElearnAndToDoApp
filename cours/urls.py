from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home , name ="home"),
    path('courses/',v.courses , name="courses"),
    path('todolist/',v.todolist , name="todolist"),
    path('dailytasks/',v.dailytasks,name="dailytasks"),
    path('updatetask/<str:pk>/',v.updateTask , name="update_task"),
    path('deletetask/<str:pk>/',v.deleteTask , name="delete_task"),
    path('donecourses/',v.donecourses, name="donecourses" ),
    path('plannedcourses/',v.plannedcourses , name = "plannedcourses"),
    path("courses/<str:id>",v.findCour , name = "courses"),
    path("setasdone/<str:id>",v.setasdone , name = "setasdone"),
]
