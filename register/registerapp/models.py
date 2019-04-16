from django.db import models

class student(models.Model):
    roll_no = models.IntegerField()
    student_name=models.CharField(max_length=20)
    marks = models.IntegerField()
    address=models.TextField(max_length=200)

    def __str__(self):
        return "%d" % self.roll_no