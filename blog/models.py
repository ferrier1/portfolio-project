from django.db import models
import datetime


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return "{}{}".format(self.text[:100], '...')

    def pub_date(self):
        return self.date.strftime('%b %e %Y')
