from django.db import models

# Creating User Models
class Users(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    Email = models.CharField(max_length=50, verbose_name="Email")
    Username = models.CharField(max_length=50, verbose_name="Username")
    Password = models.CharField(max_length=50, verbose_name="Password")
    IsAdmin = models.BooleanField(verbose_name="is admin ?", default=False)

    def __str__(self):
        return self.Email