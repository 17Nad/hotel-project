from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User, Admin, Staff, Client, Wallet


@receiver(post_save, sender = User)
def user_role(sender ,instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            Admin.objects.create(user=instance)
        elif instance.role == 'staff':
            Staff.objects.create(user=instance)
        elif instance.role == 'client':
            obj = Client.objects.create(user=instance)
            Wallet.objects.create(client = obj)