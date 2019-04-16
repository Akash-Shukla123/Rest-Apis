from rest_framework import serializers
from . models import student
from django.contrib.auth import get_user_model

class studentserializer(serializers.ModelSerializer):

    class Meta:
        model=student
        fields=('id','roll_no','student_name','marks','address')


class userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self,validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model=get_user_model()
        fields=('username','password')