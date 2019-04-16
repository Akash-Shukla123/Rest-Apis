from django.db import models

class student(models.Model):
    st_id = models.IntegerField()
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname