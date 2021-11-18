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

    board_id = models.CharField(max_length=10)
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