from django.db import models

# Create your models here.

class category(models.Model):
    Name = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.Name)

class wallpaper(models.Model):
    image = models.FileField()
    Name = models.CharField(max_length=500)
    categories = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image)
