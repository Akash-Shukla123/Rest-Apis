from rest_framework import serializers
from . models import task

class taskserializer(serializers.ModelSerializer):

    image=serializers.ImageField(max_length=None,use_url=True)
    doc=serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model=task
        fields=('id','task_name','task_desc','completed','date_created','image','doc')