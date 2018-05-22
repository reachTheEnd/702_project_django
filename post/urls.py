from django.urls import path, re_path
from  . import views
from django.contrib.auth import views as auth_view

app_name = 'post'


urlpatterns = [
    path('', views.index, name = 'index'),

    path('index/', views.IndexView.as_view(), name = 'index'),

    path('index2/', views.IndexView2.as_view(), name = 'index2'),  

    path('logined/', views.logined, name = 'logined'), 

    # path('logout/', auth_view.logout, {'next_page': 'post'}, name = 'logout'), 
    path('logout/', views.logout_view, name = 'logout'), 

    path('userlogin/', views.UerLoginForm.as_view(), name = 'userlogin'), 

    path('register/', views.UserFormView.as_view(), name = 'register'),

    re_path('(?P<Movie_information_id>[0-9]+)/', views.detail, name = 'detail'),

    # re_path('(?P<pk>[0-9]+)/', views.DetailView.as_view(), name = 'detail'),




]