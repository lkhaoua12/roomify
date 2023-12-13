"""
Module: models.py
Description: Contains Topic, Room, and Message models for handling room-related data.
"""

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Topic of the room table """
    name = models.CharField(max_length=250)

    def __str__(self):
        """ Returns string representation of the table """
        return self.name


class Room(models.Model):
    """ Room table """
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='rooms')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    def __str__(self):
        """ Returns string representation of the table """
        return self.name

    class Meta:
        ordering = ['-updated', 'created']


class Message(models.Model):
    """ Messages table """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns trimmed version of Message """
        return self.body[:50]
