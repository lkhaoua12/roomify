"""
Module: forms.py
Description: Contains RoomForm class, a Django ModelForm for Room model data.
"""

from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    """
    Class: RoomForm
    Description: Django ModelForm for Room model, excluding 'owner' and 'participants'.

    Attributes:
      - model (Room): Associated Room model.
      - fields (list): All fields included in the form.
    """
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['owner', 'participants']
