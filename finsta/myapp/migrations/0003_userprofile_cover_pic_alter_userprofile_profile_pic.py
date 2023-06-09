# Generated by Django 4.2.1 on 2023-05-27 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_userprofile_address_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='/coverpic/hairy_dog.jpg', upload_to='coverpic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_pics/eye.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
