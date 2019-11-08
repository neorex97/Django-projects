from django.db import models

#Create your models here.

class Course(models.Model):
    cname = models.CharField(max_length=20)


    def __str__(self):
        return self.cname

class Batch(models.Model):
    batch = models.CharField(max_length=120)
    b_cname = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.batch


class User(models.Model):
    Name = models.CharField(max_length=120)
    Phone = models.CharField(max_length=120)
    Batch_name = models.ForeignKey(Batch,on_delete=models.CASCADE)
    Course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.Name



class Feedback(models.Model):
    comment = models.CharField(max_length=120)
    f_batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    f_cname = models.ForeignKey(Course,on_delete=models.CASCADE)
    f_name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name,self.comment
