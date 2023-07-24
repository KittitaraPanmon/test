from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " , "+str(self.age)+" , "+self.email