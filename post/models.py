from django.db import models
from django.contrib.auth.models import Permission, User





class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)


class User_information(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	age = models.IntegerField(blank=True)
	gender = models.CharField(max_length=1, blank=True)
	occupation = models.CharField(max_length=20, blank=True)

	know_m_1 = models.CharField(max_length=100, blank=True)
	know_m_2 = models.CharField(max_length=100, blank=True)
	know_m_3 = models.CharField(max_length=100, blank=True)
	know_m_4 = models.CharField(max_length=100, blank=True)
	know_m_5 = models.CharField(max_length=100, blank=True)
	know_m_6 = models.CharField(max_length=100, blank=True)
	know_m_7 = models.CharField(max_length=100, blank=True)
	know_m_8 = models.CharField(max_length=100, blank=True)
	know_m_9 = models.CharField(max_length=100, blank=True)
	know_m_10 = models.CharField(max_length=100, blank=True)

	rec_m_1 = models.CharField(max_length=100, blank=True)
	rec_m_2 = models.CharField(max_length=100, blank=True)
	rec_m_3 = models.CharField(max_length=100, blank=True)
	rec_m_4 = models.CharField(max_length=100, blank=True)
	rec_m_5 = models.CharField(max_length=100, blank=True)
	rec_m_6 = models.CharField(max_length=100, blank=True)
	rec_m_7 = models.CharField(max_length=100, blank=True)
	rec_m_8 = models.CharField(max_length=100, blank=True)
	rec_m_9 = models.CharField(max_length=100, blank=True)
	rec_m_10 = models.CharField(max_length=100, blank=True)




		
