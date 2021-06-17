# Generated by Django 3.2.4 on 2021-06-10 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiveg', '0008_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.TextField(max_length=50)),
                ('duration', models.TextField(max_length=30)),
                ('accomplishment', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FivegPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gaps', models.TextField(max_length=100)),
                ('career_path', models.ManyToManyField(to='fiveg.CareerPath')),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
                ('type_of_qualification', models.CharField(choices=[('Academic', 'Academic'), ('Professional', 'Professional')], max_length=20)),
                ('awarding_body', models.CharField(max_length=40)),
                ('experience', models.TextField(max_length=200)),
                ('extracurricular', models.TextField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RealProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=200)),
                ('milestone', models.TextField(max_length=200)),
                ('fiveg_level', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=5)),
                ('accomplished', models.BooleanField(default=False)),
                ('resume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fiveg.resume')),
            ],
        ),
        migrations.CreateModel(
            name='LearningGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('milestone', models.TextField(max_length=200)),
                ('fiveg_level', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=5)),
                ('accomplished', models.BooleanField(default=False)),
                ('fiveg_portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiveg.fivegportfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('learning_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fiveg.learninggoal')),
                ('real_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fiveg.realprojects')),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='fiveg_portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fiveg.fivegportfolio'),
        ),
        migrations.AddField(
            model_name='resume',
            name='traditional_qualification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fiveg.traditionalqualification'),
        ),
    ]
