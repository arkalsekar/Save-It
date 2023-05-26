from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Password(models.Model):
    u_name = models.ForeignKey(User, related_name='u_name', on_delete=models.CASCADE)
    site_name = models.CharField(max_length=500, null=True, blank=True, default="Site")
    site = models.URLField(max_length=500, null=True, blank=True)
    uname_site = models.CharField(max_length=500, null=True, blank=True)
    pass_site = models.CharField(max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, null=True, blank=True)
    

    def __str__(self):
        return self.uname_site