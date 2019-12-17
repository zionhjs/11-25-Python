from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['first_name']) < 2:
            errors['first_name'] = " First Name should be at least 2 characters and letters only!"
        if len(postData['last_name']) <2:
            errors['last_name'] = "Last Name should be at least 2 characters and letters only!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors

class User(models.Model):
    email = models.CharField(max_length=125)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    total_points = models.IntegerField(default=0)
    description = models.CharField(max_length=255, default="default description")
    user_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class DailyReport(models.Model):
    recipients = models.ChoiceField()
    done  = models.CharField(max_length=255)
    challenges = models.CharField(max_length=255)
    helps = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="reports", on_delete = models.CASCADE)   #one to many
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Clock(models.Model):
    clockin = models.DateTimeField(auto_now=False)
    clockout = models.DateTimeField(auto_now=False)
    task_des = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="clocks", on_delete = models.CASCADE)   #one to many
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quote(models.Model):
    quotes = models.ChoiceField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)