from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    phone1 = models.CharField(max_length=10, null=True)
    phone2 = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=1, null=True)
    birthdate = models.DateField(null=True)
    pic = models.CharField(max_length=15, null=True)
    civil_state = models.CharField(max_length=15, null=True)
    nationality = models.CharField(max_length=15, null=True)
    id_card_number = models.CharField(max_length=15, null=True)


class Location(models.Model):
    student_id = models.ForeignKey(to=Student, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=25, null=True)
    county = models.CharField(max_length=15, null=True)
    locality = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=25, null=True)
    street_number = models.CharField(max_length=8, null=True)
    block = models.CharField(max_length=5, null=True)
    stair = models.CharField(max_length=5, null=True)
    floor = models.CharField(max_length=5, null=True)
    apartament = models.CharField(max_length=5, null=True)
    rural = models.BooleanField()


class Documents(models.Model):
    student_id = models.ForeignKey(to=Student, on_delete=models.CASCADE, null=True)
    bacalaureat_diploma = models.CharField(max_length=100, null=True)
    diploma_equivalent = models.CharField(max_length=100, null=True)
    id_card = models.CharField(max_length=100, null=True)
    birth_certificate = models.CharField(max_length=100, null=True)
    student_photo = models.CharField(max_length=100, null=True)


class Aditional_Documents(models.Model):
    document_id = models.ForeignKey(to=Documents, on_delete=models.CASCADE, null=True)
    bacalaureat_diploma = models.CharField(max_length=100, null=True)
    diploma_equivalent = models.CharField(max_length=100, null=True)
    id_card = models.CharField(max_length=100, null=True)
    birth_certificate = models.CharField(max_length=100, null=True)
    student_photo = models.CharField(max_length=100, null=True)


class Faculty(models.Model):
    name = models.CharField(max_length=25, null=True)
    short_name = models.CharField(max_length=10, null=True)
    logo = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=300, null=True)


class Section(models.Model):
    faculta_id = models.ForeignKey(to=Faculty, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=25, null=True)
    short_name = models.CharField(max_length=10, null=True)
    logo = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=300, null=True)
    

class Student_Faculty(models.Model):
    student_id = models.ForeignKey(to=Student, on_delete=models.CASCADE, null=True)
    faculty_id = models.ForeignKey(to=Faculty, on_delete=models.SET_NULL, null=True)
    section_id = models.ForeignKey(to=Section, on_delete=models.SET_NULL, null=True)
    
