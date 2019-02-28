from django.db import models

# Createyourmodelshere.
class zhuanye(models.Model):
    zname = models.CharField(verbose_name="专业",max_length=20)
    zgirlnum = models.IntegerField(verbose_name="男生数",db_column="男生数")
    zboynum = models.IntegerField(verbose_name="女生数",db_column="女生数")
    school  = models.CharField(max_length=15, null=True,verbose_name="学校",db_column="学校")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除",db_column="是否删除")
    def __str__(self):
        return self.zname
    class Meta:
        db_table="majors"
        ordering = ['id']
class student(models.Model):
    sname = models.CharField(max_length=20,db_index=True,verbose_name="姓名",db_column="姓名")
    sid = models.IntegerField(null=False,primary_key=True,default="0",verbose_name="学号",db_column="学号")
    zhuanye = models.ForeignKey('zhuanye',on_delete=models.CASCADE,null=True,verbose_name="专业",db_column="专业")
    school = models.CharField(max_length=15, null=True,verbose_name="学校",db_column="学校")
    sgender = models.BooleanField(default=False,verbose_name="性别",db_column="性别")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除",db_column="是否删除")

    def __str__(self):
        return self.sname
    class Meta:
        db_table="students"
        ordering=['sid']

# Create your models here.
