from django.db import models

# Createyourmodelshere.
class Major(models.Model):
    major = models.ForeignKey('major',on_delete=models.CASCADE,null=True,verbose_name="专业",db_column="专业")
    num_of_men = models.IntegerField(verbose_name="男生数",db_column="男生数")
    num_of_women = models.IntegerField(verbose_name="女生数",db_column="女生数")
    school  = models.CharField(max_length=15, null=True,verbose_name="学校",db_column="学校")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除",db_column="是否删除")
    def __str__(self):
        return self.major
    class Meta:
        db_table="majors"
        ordering = ['id']
class Student(models.Model):
    student_name = models.CharField(max_length=20,db_index=True,verbose_name="姓名",db_column="姓名")
    sid = models.IntegerField(null=False,primary_key=True,default="0",verbose_name="学号",db_column="学号")
    major= models.CharField(verbose_name="专业",max_length=20)
    school = models.CharField(max_length=15, null=True,verbose_name="学校",db_column="学校")
    gender = models.BooleanField(default=False,verbose_name="性别",db_column="性别")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除",db_column="是否删除")
    banji = models.CharField(max_length=15, null=True,verbose_name="班级",db_column="班级")

    def __str__(self):
        return self.student_name
    class Meta:
        db_table="students"
        ordering=['sid']
 

# Create your models here.
