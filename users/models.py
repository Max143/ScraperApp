from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# Gender Choice
	gender_choice = (
		("MALE", 'male'),
		("FEMALE", 'female'),
	)


	# Role choice
	SOFTWARE_DEVELOPER = 1
	MANAGER = 2
	WEB_DEVELOPER = 3

	role_choice = (
		(SOFTWARE_DEVELOPER, 'Software Developer'),
		(MANAGER, 'Manager'),
		(WEB_DEVELOPER, 'Web Developer'),
	)

	# Personal Detail
	job = models.CharField(max_length=100, blank=True)
	location = models.CharField(max_length=99, blank=True)
	image = models.ImageField(default='default.jpb', upload_to='profile_pics')
	gender = models.CharField(max_length=1, choices=gender_choice, blank=True)
	role = models.CharField(max_length=1 ,choices=role_choice, blank=True)


	def __str__(self):	
		return f'{ self.user.username } Profile'	


	