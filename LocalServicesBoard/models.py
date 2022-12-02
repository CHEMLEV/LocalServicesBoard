from django.db import models
from django.urls import reverse
from django.conf import settings



from datetime import datetime    



class Classified (models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    area = models.TextField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField (max_length=30, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("classified_detail", kwargs={'pk': self.pk})



