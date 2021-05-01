from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

# NB: The User will be sender, tells the Buyer to take an action if the save action
# is triggered
# The sender is acting like an instructor


@receiver(post_save, sender=User)
def create_buyer(sender, instance, created, **kwargs):
    # This means that if a user instance is created a Buyer instance to should by created
    if created:
        Buyer.objects.create(user=instance) # the user here is from the Buyer model


