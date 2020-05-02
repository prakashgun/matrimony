from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[])

# class Profile(models.Model):
#     """All information about user other than authentication"""
#
#     GENDER = (
#         ('male', _('Male')),
#         ('female', _('Female'))
#     )
#
#     PROFILE_CREATED_BY = (
#         ('self', _('Self')),
#         ('relation', _('Relation')),
#         ('friend', _('Friend'))
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dob = models.DateField()
#     about = models.TextField()
#     height = models.IntegerField()
#     weight = models.IntegerField()
