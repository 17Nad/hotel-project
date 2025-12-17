from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver
def user_role(sender, **kwargs):
    pass