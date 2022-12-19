from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Hitman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    @property
    def is_manager(self):
        if self.manager is None:
            return True
        return False


class HitStatus(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status


class Hit(models.Model):
    hitman = models.ForeignKey(Hitman, on_delete=models.CASCADE)
    target = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.ForeignKey(HitStatus, on_delete=models.CASCADE)
