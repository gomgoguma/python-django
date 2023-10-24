# 모델의 직렬화 (json)
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # 모든 필드
        # fields = ('name', 'age') # 선택한 필드
