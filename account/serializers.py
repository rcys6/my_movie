from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from account.models import Profile


class CustomUniqueValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        self.message='邮箱 %s 已经存在' % value
        return super().__call__(value, serializer_field)


class CustomUserCreateSerializer(UserCreateSerializer):
    # 验证邮箱唯一
    email=serializers.EmailField(
        validators = [ CustomUniqueValidator(queryset=User.objects.all()) ]
    )
    class Meta:
        model=User
        fields =  ('id','username','email','password') 

    def create(self,validated_data):
        user=UserCreateSerializer.create(self,validated_data)

        # 写入profile表
        profile=Profile(user=user)
        profile.save()
        return user
    
