from django.db import models

# Create your models here.


class Account(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "account"

    def __str__(self):
        return self.email
