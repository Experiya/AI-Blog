# Generated by Django 3.1.7 on 2021-05-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('is_approved', models.BooleanField(default=False)),
                ('authorId', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-timeStamp'],
                'unique_together': {('title', 'slug')},
            },
        ),
    ]
