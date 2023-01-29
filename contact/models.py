from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    subject = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
