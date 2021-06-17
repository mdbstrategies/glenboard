from django.db import models
from .choices import mentor_level, auditor_level, institution_categories,\
    traditional_qualification_types,\
    ethical_values, fiveg_levels
import uuid


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, unique=True)
    cellphone = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    geographical_zone = models.CharField(max_length=50, blank=True, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Mentor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    traditional_education = models.CharField(max_length=100)
    experience_and_accomplishments = models.TextField(max_length=500)
    ethical_values = models.TextField(max_length=500)
    motivation = models.TextField(max_length=100)
    level = models.CharField(max_length=50, choices=mentor_level)

    def __str__(self):
        return str(self.person)


class Auditor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    training = models.CharField(max_length=100)
    experience_and_accomplishments = models.TextField(max_length=500)
    motivation = models.TextField(max_length=100)
    level = models.CharField(max_length=50, choices=auditor_level)

    def __str__(self):
        return str(self.person)


class Institution(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=institution_categories)
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class TraditionalQualification(models.Model):
    qualification = models.CharField(max_length=50)
    type_of_qualification = models.CharField(max_length=20, choices=traditional_qualification_types)
    awarding_body = models.CharField(max_length=40)
    experience = models.TextField(max_length=200)
    extracurricular = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.qualification


class CareerPath(models.Model):
    career = models.TextField(max_length=50)
    duration = models.TextField(max_length=30)
    accomplishment = models.TextField(max_length=200)

    def __str__(self):
        return self.career


class FivegPortfolio(models.Model):
    career_path = models.ManyToManyField(CareerPath)
    gaps = models.TextField(max_length=100)

    def __str__(self):
        return " TODO "


class LearningGoal(models.Model):
    fiveg_portfolio = models.ForeignKey(FivegPortfolio, on_delete=models.CASCADE)
    goal = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    milestone = models.TextField(max_length=200)
    fiveg_level = models.CharField(max_length=5, choices=fiveg_levels)
    accomplished = models.BooleanField(default=False)

    def __str__(self):
        return self.goal


class Resume(models.Model):
    traditional_qualification = models.ForeignKey(TraditionalQualification, on_delete=models.SET_NULL,
                                                  null=True, blank=True)
    ethical_values = models.CharField(max_length=20, choices=ethical_values)
    fiveg_portfolio = models.ForeignKey(FivegPortfolio, on_delete=models.SET_NULL,
                                        null=True, blank=True)

    def __str__(self):
        return "TODO"


class RealProjects(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL,
                               null=True, blank=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    milestone = models.TextField(max_length=200)
    fiveg_level = models.CharField(max_length=5, choices=fiveg_levels)
    accomplished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Deliverable(models.Model):
    learning_goal = models.ForeignKey(LearningGoal, on_delete=models.CASCADE,
                                      null=True, blank=True)
    real_project = models.ForeignKey(RealProjects, on_delete=models.CASCADE,
                                     null=True, blank=True)
    description = models.CharField(max_length=50)
    attachment = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.description
