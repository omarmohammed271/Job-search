# Generated by Django 4.2.2 on 2023-07-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='cover_letter',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apply',
            name='cv',
            field=models.FileField(default=1, upload_to='apply/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apply',
            name='published',
            field=models.DateField(auto_now=True),
        ),
    ]
