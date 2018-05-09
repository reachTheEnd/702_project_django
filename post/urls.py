from django.urls import path
from  . import views
 
app_name = 'post'


urlpatterns = [
    path('', views.index, name = 'index'),  
    path('register/', views.UserFormView.as_view(), name = 'register'),  

]