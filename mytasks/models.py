from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    temperature = models.FloatField()
    condition = models.TextField()
    query_datetime = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.city+'_'+str(self.id)