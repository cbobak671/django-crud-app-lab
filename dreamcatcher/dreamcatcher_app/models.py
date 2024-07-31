from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    ('R', 'Dream'),
    ('N', 'Nightmare'),
    ('D', 'Daydream'),
)

TAGS = (
    ('S', 'Same'),
    ('D', 'Different'),
    ('H', 'Hybrid: Same+Different')
)
# Create your models here.

class Dream(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    description = models.TextField(max_length=1000)
    date = models.DateField('Dream date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dream_detail", kwargs={"dream_id": self.id})
    
    
    class Meta:
        ordering = ['-date']

class DreamHistory(models.Model):
    date = models.DateField('Dream date')
    tag = models.CharField(
        max_length=1,
        choices=TAGS,
        default=TAGS[0][0]
    )
    description = models.TextField(
        max_length=100,
        default=''
    )

    dream = models.ForeignKey(Dream, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_tag_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
    
