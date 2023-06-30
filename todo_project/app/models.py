from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    staus_choice = [
        ('C','Completed'),
        ('P','Pending'),
    ]
    
    priority_choice = [
        ('1','1️⃣'),
        ('1','2️⃣'),
        ('1','3️⃣'),
        ('1','4️⃣'),
        ('1','5️⃣'),
        ('1','6️⃣'),
        ('1','7️⃣'),
        ('1','8️⃣'),
        ('1','9️⃣'),
        ('1','🔟'),

    ]
    
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2,choices=staus_choice)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    priority = models.CharField(max_length=10,choices=priority_choice)
