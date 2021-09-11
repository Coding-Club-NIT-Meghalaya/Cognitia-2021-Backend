from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.


class Year(models.Model):
    year = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.year)


class Event(models.Model):
    TYPE_CHOICES = (
        ("Coding", "Coding"),
        ("Robotics", "Robotics"),
        ("Departmental", "Departmental"),
        ("Gaming", "Gaming"),
    )
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(
        max_length=200, choices=TYPE_CHOICES, default='Coding')
    duration = models.CharField(max_length=20)
    total_prize = models.CharField(max_length=100)
    registration_link = models.CharField(max_length=100)
    year = models.ForeignKey(
        Year, on_delete=models.PROTECT, related_name='event_year')
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=200)
    meet_link = models.CharField(max_length=100)
    doc_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    POSITION_CHOICES = (
        ("Coordinator", "Coordinator"),
        ("Co-Coordinator", "Co-Coordinator"),
    )
    member_name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100, choices=POSITION_CHOICES, default='Coordinator')
    email = models.EmailField(max_length=100)
    image = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    event_name = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name='team_members')


class Gallery(models.Model):
    image = models.CharField(max_length=200)
