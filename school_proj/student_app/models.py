from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, blank = False)
    student_email = models.EmailField(unique=True, null=False, blank=False)
    personal_email = models.EmailField(blank = True, unique=True, null=True)
    locker_number = models.IntegerField(default=110, blank = False, unique=True)
    locker_combination = models.CharField(max_length=255, blank = False, default="12-12-12")
    good_student = models.BooleanField(blank=False, default=True)

    def __str__(self):
        f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_num):
        self.locker_number = new_locker_num

    def student_status(self, qualification):
        self.good_student = qualification