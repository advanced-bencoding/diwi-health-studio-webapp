# Generated by Django 4.0.2 on 2022-03-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_staff_department'),
        ('blog', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='written_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.staff'),
        ),
    ]
