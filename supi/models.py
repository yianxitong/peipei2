from django.db import models

# Createyourmodelshere.
class zhuanye(models.Model):
    zname = models.CharField(max_length=20)
    zgirlnum = models.IntegerField()
    zboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

class student(models.Model):
    sname = models.CharField(max_length=20,db_index=True)
    sid = models.IntegerField(db_index=True)
    szhuanye= models.ForeignKey("zhuanye",on_delete=models.CASCADE)

    isDelete = models.BooleanField(default=False)
    ordering=['sid']



# Create your models here.
