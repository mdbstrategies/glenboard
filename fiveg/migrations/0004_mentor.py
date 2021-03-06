# Generated by Django 3.2.3 on 2021-06-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiveg', '0003_alter_person_geographical_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('traditional_education', models.CharField(max_length=100)),
                ('experience_and_accomplishments', models.TextField(max_length=500)),
                ('ethical_values', models.TextField(max_length=500)),
                ('motivation', models.TextField(max_length=100)),
                ('level', models.CharField(choices=[('Yellow Belt', 'Yellow Belt'), ('Green Belt', 'Green Belt'), ('Red Belt', 'Red Belt'), ('Black Belt', 'Black Bet')], max_length=50)),
            ],
        ),
    ]
