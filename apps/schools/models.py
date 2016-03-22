from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	created_at = models.DateTimeField()
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'students'

class Teacher(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	created_at = models.DateTimeField()
	def __str__(self):
		return "%s is a teacher" % (self.name)

	class Meta:
		db_table = 'teachers'

class Subject(models.Model):
	name = models.CharField(max_length=200)
	teacher = models.ForeignKey(Teacher)
	created_at = models.DateTimeField()
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'subjects'