from django.db import models

class pClass(models.Model):
	class_name = models.CharField(max_length=200)
	year_crossed = models.CharField(max_length=200)

	def __str__(self):
		return self.pledge_class

class brother(models.Model):
	name = models.CharField(max_length=200)
	pledge_class = models.ForeignKey(pClass, related_name='brothers')
	pledge_name = models.CharField(max_length=200)
	line_number = models.IntegerField(max_length=10)

	def __str__(self):
		return self.name
