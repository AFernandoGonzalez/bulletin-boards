from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# 



class Board(models.Model):

    LowTraffic = 1
    MediumTraffic = 2
    HighTraffic = 3

    STATUS_CHOICES = (
        (LowTraffic, "Low Traffic"),
        (MediumTraffic, "Medium Traffic"),
        (HighTraffic, "High Traffic"),
    )

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='boards_pics/', blank=False)
    total_flyers = models.CharField(max_length=100, null=True, blank=True)
    total_posted = models.CharField(max_length=100, null=True, blank=True)
    space_available = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='office_pics/', blank=False)
    # add a user here / updaetd by current user
    updated_by = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Flyer(models.Model):
    Saa = 1
    Submission = 2

    Yes = 1
    No = 2

    CREATOR_CHOICES = (
        (Saa, "Student Affairs"),
        (Submission, "External Office"),
    )

    added_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    board = models.ManyToManyField(Board)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='flyer_pics/', blank=False)
    removed = models.BooleanField(default=False)
    flyer_creator = models.IntegerField(choices=CREATOR_CHOICES, blank=True, null=True)
    flyer_edited = models.IntegerField(choices=CREATOR_CHOICES, blank=True, null=True)
    # add a due date  
    date_posted = models.DateField(null=True)
    # add a due date
    due_date = models.DateField(null=True)
    # add a user here / updaetd by current user
    updated_by = models.CharField(max_length=200, null=True, blank=True)
    # status of this flyer / posted? yes no


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
