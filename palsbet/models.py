from django.db import models

from django.utils import timezone

import datetime

from django.conf import settings

from django.contrib.auth.models import User

from django.conf import settings

from django.contrib.auth.models import User

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

class Visitor(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, null=False, related_name='visitor', on_delete=models.CASCADE,)
    session_key = models.CharField(null=False, max_length=40)

class Jackpot(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    Number = models.PositiveIntegerField(default = 0)

    Home_Team = models.CharField(max_length = 200)

    Home_Odds = models.CharField(max_length = 50, null = True)

    Draw = models.CharField(max_length = 50, null = True)

    Away_Team = models.CharField(max_length = 200)

    Away_Odds = models.CharField(max_length = 50, null = True)

    Prediction = models.CharField(max_length = 100, null = True, choices=[('Running','Running'),('Home','Home'),('Draw','Draw'),('Away','Away')])

    def __str__(self):
       return self.Home_Team

class FreeTipsGames(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    country = models.CharField(max_length = 200)

    home_team = models.CharField(max_length = 200)

    home_score = models.PositiveIntegerField(default = 0)

    away_score = models.PositiveIntegerField(default = 0)

    away_team = models.CharField(max_length = 200)

    prediction = models.CharField(max_length = 100)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team



class SingleBetGames(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    country = models.CharField(max_length = 200)

    home_team = models.CharField(max_length = 200)

    home_score = models.PositiveIntegerField(default = 0)

    away_score = models.PositiveIntegerField(default = 0)

    away_team = models.CharField(max_length = 200)

    prediction = models.CharField(max_length = 100)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team

class VipTips(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    country = models.CharField(max_length = 200)

    home_team = models.CharField(max_length = 200)

    home_score = models.PositiveIntegerField(default = 0)

    away_score = models.PositiveIntegerField(default = 0)

    away_team = models.CharField(max_length = 200)

    prediction = models.CharField(max_length = 100)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team


class PunterPick(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    country = models.CharField(max_length = 200)

    home_team = models.CharField(max_length = 200)

    home_score = models.PositiveIntegerField(default = 0)

    away_score = models.PositiveIntegerField(default = 0)

    away_team = models.CharField(max_length = 200)

    prediction = models.CharField(max_length = 100)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team


class RollOver(models.Model):

    published_date = models.DateTimeField('Date Published', auto_now_add=True)

    country = models.CharField(max_length = 200)

    home_team = models.CharField(max_length = 200)

    home_score = models.PositiveIntegerField(default = 0)

    away_score = models.PositiveIntegerField(default = 0)

    away_team = models.CharField(max_length = 200)

    prediction = models.CharField(max_length = 100)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team

class Notification(models.Model):
       Head = models.TextField(blank=True, null=True)
       Body = models.TextField(blank=True, null=True)
       published_date = models.DateTimeField('Date Published', auto_now_add=True)

       def __str__(self):
          return self.Head
