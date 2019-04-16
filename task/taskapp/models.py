from django.db import models

class task(models.Model):
    task_name=models.CharField(max_length=20)
    task_desc=models.TextField(max_length=200)
    completed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/', default='images/none/no-img.jpg')
    doc=models.FileField(upload_to='doc/',default='doc/None/no-doc.pdf')

    def __str__(self):
     return "%s" % self.task_name

