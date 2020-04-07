from rest_framework import serializers
from rankings import models
class userserializers(serializers.ModelSerializer):
    class Meta:
        """model 指你所要操作的表"""
        model = models.User
        fields = '__all__'
