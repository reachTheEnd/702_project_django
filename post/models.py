from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse





class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)

class Movie_information(models.Model):
	name = models.CharField(max_length=100, blank=True)
	date = models.CharField(max_length=100, blank=True)
	website = models.CharField(max_length=100, blank=True)

	def get_absolute_url(self):
		return reverse('movie: detail', kwargs={'pk':self.pk})


	def __str__(self):
		return self.name + '-' + self.date


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




		
