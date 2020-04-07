from django.db import models

# Create your models here.
class User(models.Model):
    """客户端号"""
    name = models.CharField(max_length=32)
    """分数"""
    grade = models.IntegerField(max_length=11)
    class Meta:
        db_table = 'user'