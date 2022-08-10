from django.db import models

class Motor(models.Model):
    channel_no = models.SmallIntegerField(default = 0)
    value=models.FloatField(default = 0)
    motor_name = models.CharField(max_length=200, default='null')
    
    def __str__(self):
        if self.motor_name=='null':
            return f'Motor {self.pk} on channel {self.channel_no}'
        else:
            return self.motor_name

# Create your models here.
