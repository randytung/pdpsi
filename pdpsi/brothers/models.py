from django.db import models

class PClass(models.Model):
	class_name = models.CharField(max_length=200)
	year_crossed = models.CharField(max_length=200)

	def __str__(self):
		return self.class_name

class Brother(models.Model):
	name = models.CharField(max_length=200)
	pledge_class = models.ForeignKey(PClass, related_name='brothers')
	pledge_name = models.CharField(max_length=200)
	line_number = models.IntegerField(default=0)
	active = models.BooleanField()

	def __str__(self):
		return self.name
