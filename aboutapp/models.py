from django.db import models


class Count(models.Model):
    years = models.IntegerField(default=0)
    projectCompeletes = models.IntegerField(default=0)
    Smiles = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.years} - {self.projectCompeletes} - {self.Smiles}"



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
