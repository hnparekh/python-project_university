
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
 
    M = 1
    F = 0
    GENDER = (
               (M, "MALE"),
               (F, "FEMALE"),
    )
    gender = models.IntegerField(choices=GENDER, max_length=1, default=M)       
   
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
   
    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.address


class Marks(models.Model):
    student = models.ForeignKey(Student)

    ENGLISH = 1
    MATHS = 2
    PHYSICS = 3

    SUBJECTS = (
        (ENGLISH, "English"),
        (MATHS, "Mathematics"),
        (PHYSICS, "Physics"),
    )
    subject = models.IntegerField(choices=SUBJECTS)
    marks = models.IntegerField()