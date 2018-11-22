from rest_framework import serializers
from .models import *


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('id', 'name',)


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name',)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'roleid', 'login', 'password', 'email', 'dateofadd', 'phone',)


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'departmentsid',)


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('id', 'name', 'categoryid', 'price', 'description',)


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'name',)


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'waiterid', 'tablesid', 'statusid', 'mealsid', 'tablesname', 'date',)


class MealsToOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrders
        fields = ('id', 'count', 'orderid', 'mealsid',)


class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('id', 'name',)


class ChecksSerializer(serializers.ModelSerializer):
    totalsum = serializers.SerializerMethodField()

    def get_totalsum(self, request):
        sum = 0
        mto = MealsToOrders.objects.filter(orderid=request.orderid)
        for s in mto:
            sum += s.count * s.mealsid.price
        return sum

    class Meta:
        model = Checks
        fields = ('id', 'orderid', 'percentage', 'date', 'mealsid', 'totalsum',)

