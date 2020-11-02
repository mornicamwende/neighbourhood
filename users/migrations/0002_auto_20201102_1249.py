# Generated by Django 3.1.2 on 2020-11-02 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0003_auto_20201102_1249'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='welome to my hood', max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='home',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.home'),
        ),
    ]
