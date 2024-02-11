from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table="user"
    def __str__(self):
        return self.username +" | "+self.email+" | "+ self.password
