from django.db import models

# Create your models here.


class Year(models.Model):
    year = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.year


class Prize(models.Model):
    scope = models.CharField(max_length=100)
    prize1 = models.IntegerField()
    prize2 = models.IntegerField()
    prize3 = models.IntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return "Prize 1: Rs."+str(self.prize1)+"  Prize 2: Rs."+str(self.prize2)+"  Prize 3: Rs."+str(self.prize3)


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=200)
    start_time = models.TimeField()
    duration = models.CharField(max_length=20)
    year = models.ForeignKey(
        Year, on_delete=models.PROTECT, related_name='event_year')
    prize = models.ForeignKey(
        Prize, on_delete=models.PROTECT, related_name='prize')
    description = models.CharField(max_length=500)
    rules = models.CharField(max_length=200)
    judging_parameter = models.CharField(max_length=500)
    registration_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    member_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='images')
    event_name = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name='team_members')
