# Generated by Django 2.1.7 on 2019-04-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20190414_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='images/none/no-img.jpg', upload_to='images/'),
        ),
    ]
