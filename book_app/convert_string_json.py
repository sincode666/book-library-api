from rest_framework import serializers
from .models import book_str
class book_str_converted(serializers.ModelSerializer):
    class Meta:
        model = book_str
        fields = '__all__'