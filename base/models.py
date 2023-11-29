from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Topic of the room table """
    name = models.CharField(max_length=250)

    def __str__(self):
        """ returns string rep of table """
        return self.name


class Room(models.Model):
    """ the room table """
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """ returns string rep of table """
        return self.name


class Message(models.Model):
    """ the messages table """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ returns trimmed version of Message """
        return self.body
