from django.db import models

class Club(models.Model):
    name = models.CharField(("Name"), max_length=50)
    money = models.IntegerField(("Money"))

    def __str__(self):
        return f"{self.name}-{self.money}"
