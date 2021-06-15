from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

