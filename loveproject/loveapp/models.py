from django.db import models


class Couple(models.Model):
    name_a = models.CharField(max_length=100, blank=True, null=True)
    name_b = models.CharField(max_length=100, blank=True, null=True)
    photo_a = models.ImageField(upload_to='uploads/', blank=True, null=True)
    photo_b = models.ImageField(upload_to='uploads/', blank=True, null=True)
    percent = models.IntegerField()
    sentence = models.TextField()
    tips = models.TextField()
    score = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_a or 'PhotoA'} ❤️ {self.name_b or 'PhotoB'}"
