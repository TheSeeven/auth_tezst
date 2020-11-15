from django.db import models

# Create your models here.


class User(models.Model):
    username            = models.CharField(max_length = 35)
    password            = models.CharField(max_length = 100)
    email               = models.EmailField()
    first_name          = models.CharField(max_length = 25)
    last_name           = models.CharField(max_length = 25)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Token(models.Model):
    username            = models.ForeignKey(to = User, on_delete = models.CASCADE)
    token               = models.CharField(max_length=100)


class Faculty(models.Model):
    nume                = models.CharField(max_length = 25)
    description         = models.CharField(max_length = 300)


class Section(models.Model):
    faculty_id          = models.ForeignKey(to = Faculty, on_delete = models.CASCADE)
    nume                = models.CharField(max_length = 25)
    descriere           = models.CharField(max_length = 100)


class Student(models.Model):
    user_id             = models.ForeignKey(to = User, on_delete = models.CASCADE, null=True)
    county              = models.CharField(max_length = 15)
    locality            = models.CharField(max_length = 20)
    street              = models.CharField(max_length = 25)
    street_number       = models.CharField(max_length=8)
    block               = models.CharField(max_length = 5)
    staircase           = models.CharField(max_length = 5)
    floor               = models.CharField(max_length = 5)
    apartament          = models.CharField(max_length = 5)
    rural               = models.BooleanField()
    phone1              = models.CharField(max_length = 10)
    phone2              = models.CharField(max_length = 10)
    diploma             = models.CharField(max_length = 100)
    id_card             = models.CharField(max_length = 100)
    faculty_id          = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    section_id          = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
