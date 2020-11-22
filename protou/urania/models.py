from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length= 128, unique=True)
    emocion = models.CharField(max_length= 128)

    def __str__(self):
        name = self.word
        emocion = self.emocion
        return '{} - {}'.format(name, emocion)

class Vote(models.Model):
    vote = models.IntegerField(null = True)
    word = models.ForeignKey(Word, on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

    def __str__(self):
        vote = self.vote
        word = self.word
        user = self.user
        return "{} voted {} on word {}".format(user, vote, word)

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    attempts = models.IntegerField(default=0)
    current_words = models.CharField(max_length=1024)
    def __str__(self):
        return "{}".format(self.user)
