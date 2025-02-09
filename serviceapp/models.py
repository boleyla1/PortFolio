from django.db import models


class Faq(models.Model):
    Question = models.TextField()
    Answer = models.TextField()

    def __str__(self):
        return self.ques

# Create your models here.
