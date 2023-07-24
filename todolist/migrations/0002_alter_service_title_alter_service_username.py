# Generated by Django 4.2 on 2023-07-24 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.user'),
        ),
    ]
