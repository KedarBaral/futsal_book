from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    place = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    team = models.CharField(max_length=20, default='abc')

    def __str__(self):
        return self.name, str(self.age), self.place, self.phone_no, self.team


