from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length = 250)
    RollNo = models.CharField(max_length = 10, unique = True)
    Email = models.EmailField(max_length = 200)
    Password = models.CharField(max_length = 200)
    Url = models.URLField(blank = True)
    DOB = models.DateField(blank = True)

    class Meta:
        verbose_name_plural = "Student"

    def __str__(self):
        return self.Name
