from rest_framework import generics
from users.models import Roles
from .serializers import *
from .models import *


class MealsViewSet(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DepartmentsViewSet(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class RolesViewSet(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class RolesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class TablesViewSet(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class TablesDetailView(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class OrdersViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServicePercentageViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ServicePercentageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class ChecksViewSet(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer


class ChecksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer


class StatusesViewSet(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class StatusesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class MealsToOrdersViewSet(generics.ListCreateAPIView):
    queryset = MealsToOrders.objects.all()
    serializer_class = MealsToOrdersSerializer


class MealsToOrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealsToOrders.objects.all()
    serializer_class = MealsToOrdersSerializer


class MealsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


