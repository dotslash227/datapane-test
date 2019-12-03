from django.db import models


# Initially decided to go with dynamic menu items, but left it.
class Navigation(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Model for entry form.
class Entries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name