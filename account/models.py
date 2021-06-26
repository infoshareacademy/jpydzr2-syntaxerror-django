from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    married = models.IntegerField(blank=True, null=True)
    education = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_num = models.CharField(max_length=16, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    str_building_no = models.CharField(max_length=10, blank=True, null=True)
    str_local_no = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
