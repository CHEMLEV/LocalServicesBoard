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


class Review (models.Model):

    classified = models.ForeignKey(Classified, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6, 1)])
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        if self.rating == 1: 
            rate = "⭐︎"
        elif self.rating == 2:
            rate = "⭐︎⭐︎"
        elif self.rating == 3:
            rate = "⭐︎⭐︎⭐︎"
        elif self.rating == 4:
            rate = "⭐︎⭐︎⭐︎⭐︎"
        elif self.rating == 5:
            rate = "⭐︎⭐︎⭐︎⭐︎⭐︎"
        else:
            rate = ""
        
        return  rate + " " + self.title + " : " + self.body + " : " + self.date.date # + " Star " + str(self.rating) + " title:"

    def get_absolute_url(self):
        return reverse ("classified_detail", kwargs={'pk': self.pk})




