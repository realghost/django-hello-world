from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    jabber = models.EmailField(blank=True)
    skype = models.CharField(blank=True, max_length=30)
    bio = models.TextField(blank=True)
    other_contacts = models.TextField(blank=True)