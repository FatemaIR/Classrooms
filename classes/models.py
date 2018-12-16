from django.db import models
from django.urls import reverse
from model_utils import Choices
from datetime import date
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	GENDER_CHOICES = Choices('Male', 'Female')
	gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
	exam_grade = models.FloatField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name


