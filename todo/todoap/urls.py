from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addtodo',views.addtodo,name="addtodo"),
    path('login_user',views.login_user,name="login_user"),
    path('signup_user',views.signup_user,name="signup_user"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('add_todo',views.add_todo,name='add_todo'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('complete_todo/<int:id>',views.complete_todo,name='complete_todo'),
    
]