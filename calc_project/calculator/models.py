from django.db import models

class Calculator_machine(models.Model):
	result = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.result
