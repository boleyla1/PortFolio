from django.db import models


class Faq(models.Model):
    Question = models.TextField()
    Answer = models.TextField()

    def __str__(self):
        return self.Question

# Create your models here.
