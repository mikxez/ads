from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Exchange(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен')
    ]
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_exchanges')
    to_ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='exchange_requests')
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)