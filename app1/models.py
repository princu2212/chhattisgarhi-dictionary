from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query = models.TextField()

class AddWord(models.Model):
    hindi = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    chhattisgarhi = models.CharField(max_length=50)
    

    


    
