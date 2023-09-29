from django.db import models

# Create your models here.
class school(models.Model):
    schlname=models.CharField(max_length=100,primary_key=True)
    principal=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.schlname


class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=50)
    semail=models.EmailField()
    schlname=models.ForeignKey(school,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
    