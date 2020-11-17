from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password, first_name, last_name):
        if not email:
            raise "Email is required"
        if not username:
            raise "Username is required"
        if not password:
            raise "Password is required"
        if not first_name:
            raise "A first name is required"
        if not last_name:
            raise "A last name is required"
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=35, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name',]
    
    objects = MyUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return True



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
    
