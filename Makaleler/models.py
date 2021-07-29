from django.db import models

from django.db import models

# Create your models here.
class Yazılar(models.Model):
    AnaBaslık = models.CharField(max_length=200)
    AltBaslık = models.CharField(max_length=200)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=None)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.AnaBaslık