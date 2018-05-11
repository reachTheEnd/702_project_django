from django.urls import path
from  . import views
from django.contrib.auth import views as auth_view

app_name = 'post'


urlpatterns = [
    path('', views.index, name = 'index'), 

    path('logined/', views.logined, name = 'logined'), 

    # path('logout/', auth_view.logout, {'next_page': 'post'}, name = 'logout'), 
    path('logout/', views.logout_view, name = 'logout'), 

    path('userlogin/', views.UerLoginForm.as_view(), name = 'userlogin'), 

    path('register/', views.UserFormView.as_view(), name = 'register'),  

]