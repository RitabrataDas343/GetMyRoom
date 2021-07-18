# Generated by Django 3.0.3 on 2020-03-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_roomimage_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_image',
            field=models.ImageField(default=None, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rooms',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='RoomImage',
        ),
    ]