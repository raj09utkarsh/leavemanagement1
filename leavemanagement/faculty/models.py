from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    DEPARTMENT = (
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('ME', 'ME')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=3, choices=DEPARTMENT)
    # is_hod = models.BooleanField(default=False)
    level = models.IntegerField(default=2)

    def __str__(self):
        return self.user.username