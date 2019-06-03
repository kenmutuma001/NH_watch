from django import forms
from .models import *


class AddAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('area_name', 'area_photo', 'population')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'neighborhood')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name', 'email', 'area')


class Notification(forms.ModelForm):
    class Meta:
        model= Notification
        fields = ('title', 'posted_by', 'area')
