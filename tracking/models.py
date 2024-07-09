from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    user_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user_id


class Profile(models.Model):
    profile_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.profile_id


class Activity(models.Model):
    activity_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    distance = models.FloatField()
    date = models.DateField()
    calories_burned = models.IntegerField()

    def __str__(self):
        return self.activity_id


class WorkoutPlan(models.Model):
    plan_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    goals = models.TextField()

    def __str__(self):
        return self.plan_id


class WorkoutSession(models.Model):
    session_id = models.CharField(max_length=255, primary_key=True)
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.session_id


class Goal(models.Model):
    goal_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()
    is_achieved = models.BooleanField()

    def __str__(self):
        return self.goal_id


class Progress(models.Model):
    progress_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    body_fat_percentage = models.FloatField()
    muscle_mass = models.FloatField()

    def __str__(self):
        return self.progress_id
