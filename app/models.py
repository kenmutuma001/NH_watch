from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Area(models.Model):
    area_name = models.CharField(max_length=50, blank=True)
    area_photo = models.ImageField(upload_to='pics/')
    population = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.area_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_neighborhood(self, neigborhood_id):
        self.search_by_id(id=neigborhood_id)

    def update_neighborhood(self):
        self.update_area()

    def update_occupants(self):
        self.update_population()


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    business_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.area

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self, business_id):
        self.search_by_id(id=business_id)

    def update_business(self):
        self.update()


class Notification(models.Model):
    title = models.CharField(max_length=500, blank=True)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)
