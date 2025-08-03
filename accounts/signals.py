from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppUser, Profile

@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)