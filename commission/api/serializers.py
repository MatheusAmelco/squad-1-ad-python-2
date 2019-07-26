from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Commission_plan, Sellers, Sales


class CommissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission_plan
        fields = ['id', 'lower_percentage', 'upper_percentage', 'min_value']


class SellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = ['id', 'name', 'address', 'phone', 'age', 'email', 'cpf', 'plan']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id', 'month', 'amount', 'commission', 'sellers_id']


class CheckCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['amount', 'sellers_id']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
