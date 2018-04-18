from django.db import models
import datetime


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()

    def summary(self):
        return "{}{}".format(self.text[:100], '...')
