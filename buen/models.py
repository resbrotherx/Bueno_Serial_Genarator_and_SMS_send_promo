from django.db import models
from django.contrib.auth.models import User

class Genarator(models.Model):
	STATUS_CHOICES = (('Inactive','Inactive'), ('Active','Active'), ('Sold','Sold'))
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	genarator = models.CharField(max_length=900)
	date_created = models.DateField(auto_now=True)
	time_created = models.TimeField(auto_now=True)
	date_time = models.DateTimeField(auto_now=True)
	stock = models.CharField(max_length=400, choices=STATUS_CHOICES, default='Inactive')
  
	def __str__(self):
		return self.genarator

class SoledSerial(models.Model):
	STATUS_CHOICES = (('Inactive','Inactive'), ('Active','Active'), ('Sold','Sold'))

	contact = models.CharField(max_length=15) 
	serial_number = models.CharField(max_length=200)
	date_time = models.DateTimeField(auto_now=True)
	winner = models.BooleanField(default=False)
	validation = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	status = models.CharField(max_length=400, choices=STATUS_CHOICES, default='Sold')
	date_created = models.DateField(auto_now=True)
	time_created = models.TimeField(auto_now=True)
	date_sold = models.DateField(auto_now_add=True)
	time_sold = models.TimeField(auto_now_add=True)
	
	def __str__(self):
		return self.contact 

class Promo(models.Model):
	STATUS_CHOICES = (('Inactive','Inactive'), ('Active','Active'), ('Sold','Sold'))

	contact = models.CharField(max_length=15) 
	serial_number = models.CharField(max_length=200)
	winner = models.BooleanField(default=True)
	date_time = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=400, choices=STATUS_CHOICES, default='Sold')
	date_created = models.DateField(auto_now=True)
	time_created = models.TimeField(auto_now=True)
  
	def __str__(self):
		return self.serial_number 

class Customer(models.Model):
	STATUS_CHOICES = (('In Stock','In Stock'), ('Out of stock','Out of stock'), ('Running Out of stock','Running Out of stock'))

	staff = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100) 
	email = models.EmailField()  
	contact = models.CharField(max_length=15) 
	serial_number = models.CharField(max_length=200)
	winner = models.CharField(max_length=200)
	stock = models.CharField(max_length=400, choices=STATUS_CHOICES, default='In Stock')
	date_created = models.DateField(auto_now=True)
	time_created = models.TimeField(auto_now=True)
	date_sold = models.DateField(auto_now=False)
	time_sold = models.TimeField(auto_now=False)
  
	def __str__(self):
		return self.serial_number 

	class Meta:
		db_table = "customer"

class Archive(models.Model):
	staff = models.ForeignKey(User, on_delete=models.CASCADE)
	serial_no = models.ForeignKey(SoledSerial, on_delete=models.CASCADE)
	date_created = models.DateField(auto_now=True)
	time_created = models.TimeField(auto_now=True)
	date_time = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.staff) + " " + str(self.serial_no)