from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Car
import uuid
from buyers.models import Buyer

# @receiver(pre_save, sender=Car) # the car is the sender and also the reciver
# def buyer_modify_code(sender, instance, **kwargs):
#     # NB created is not included because we won't have access to it
#     if instance.code == "":
#         instance.code = str(uuid.uuid4()).replace('-', '').upper()[:10]

#     # setting user name of buyer to buyer of car
#     obj = Buyer.objects.get(user=instance.buyer.user)
#     obj.from_signal = True
#     obj.save()

@receiver(post_save, sender=Car) # the car is the sender and also the reciver
def buyer_modify_code(sender, created, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace('-', '').upper()[:10]
        instance.save()
    # setting user name of buyer to buyer of car
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()

# NB we did not check 'if created' because sender and the reciever are the same