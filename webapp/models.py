from django.db import models

# Create your models here.

class Streamer(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    operator=models.CharField(max_length=20)
    data_stream=models.FloatField()
    class Meta:
        ordering = ['-timestamp']
    

    def __str__(self):
        return self.operator