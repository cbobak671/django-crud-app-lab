# Generated by Django 4.2.14 on 2024-07-31 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('R', 'Dream'), ('N', 'Nightmare'), ('D', 'Daydream')], default='R', max_length=1)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField(verbose_name='Dream date')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
