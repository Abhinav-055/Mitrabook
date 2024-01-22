from django.db import models
class Newuser(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   username = models.CharField(max_length=15)
   password = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name
class Message(models.Model):
   sender = models.CharField(max_length=50,default='')
   receiver = models.CharField(max_length=50,default='')
   content = models.TextField(default='')
    
   def __str__(self):
      return f"{self.sender} to {self.receiver} - {self.timestamp}"


