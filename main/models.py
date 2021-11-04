from django.db import models
from .constants import *

class Account(models.Model):
	BOT_STEPS = StepsMixin().BOT_STEPS
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	user_id = models.CharField(max_length=12)
	bot_steps = models.CharField(choices=BOT_STEPS,max_length=100,default=BOT_STEPS[0][0])
