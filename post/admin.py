from django.contrib import admin
from .models import Employee, User_information, Movie_information
# Register your models here.
admin.site.register(Employee)
admin.site.register(User_information)
admin.site.register(Movie_information)