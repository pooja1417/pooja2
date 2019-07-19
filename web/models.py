from django.db import models


class Roles(models.Model):
	Role=models.CharField(max_length=30)
	Department=models.CharField(max_length=30)
	Location=models.CharField(max_length=30)


	def __str__(self):
		return self.Role
		return self.Department
		return self.Location