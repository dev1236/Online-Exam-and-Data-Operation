from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
##class names:
    ##name : str
    #mobile : int
    #img : str

class Register(models.Model):  
    img:str
    username = models.CharField(max_length=20)  
    email= models.EmailField() 
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=8)
    class Meta:  
        db_table = "Register"

class upload_doc(models.Model):
    item_name = models.CharField(max_length=100)
    item_amount = models.IntegerField()
    item_desc = models.TextField()
    images = models.ImageField(upload_to='MEDIA_ROOT/images/')  
    class Meta:
        db_table="upload_doc"

class student_data(models.Model):
    user_name = models.CharField(max_length=20)
    st_name = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    college = models.CharField(max_length=40)
    branch = models.CharField(max_length=10)
    semester = models.IntegerField()
    photo = models.ImageField(upload_to='media/images',blank=True)
    signature =models.ImageField(upload_to='media/images',blank=True)
    usn = models.CharField(max_length=10)
    class Meta:
        db_table = "student_data"
    def __str__(self):
        return self.st_name



class questions(models.Model):
    question_id = IntegerField()
    question_name = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=20)
    option_2 = models.CharField(max_length=20)
    option_3 = models.CharField(max_length=20)
    option_4 = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    class Meta:
        db_table = "questions"


class user_submit(models.Model):
    student_name  = models.CharField(max_length=30)
    student_mobile = models.IntegerField()
    answer = models.CharField(max_length=200)
    
    class Meta:
        db_table = "user_submit"