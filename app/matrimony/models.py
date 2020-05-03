from django.db import models


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class PhysicalStatus(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class BodyType(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Complexion(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class CreatedBy(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class EatingHabit(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class DrinkingHabit(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class SmokingHabit(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Caste(models.Model):
    name = models.CharField(max_length=255)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Star(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Raasi(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Dosham(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class EmployedIn(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class CurrencyType(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class FamilyValue(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class FamilyType(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class FamilyStatus(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

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
