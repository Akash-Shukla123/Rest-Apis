# Generated by Django 2.1.7 on 2019-04-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='doc',
            field=models.FileField(default='doc/None/no-doc.pdf', upload_to='doc/'),
        ),
    ]
