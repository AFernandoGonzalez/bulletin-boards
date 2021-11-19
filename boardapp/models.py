from django.db import models


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
    total_flyers = models.CharField(max_length=100)
    total_posted = models.CharField(max_length=100)
    space_available = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='office_pics/', blank=False)

    def __str__(self):
        return self.name


class Flyer(models.Model):
    board = models.ManyToManyField(Board)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='flyer_pics/', blank=False)


    def __str__(self):
        return self.name
