from django.db import models
from users.models import User


class Tables(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return self.name


# class Roles(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Название')
#
#     class Meta:
#         verbose_name = 'Должность'
#         verbose_name_plural = 'Должности'
#
#     def __str__(self):
#         return self.name


# class Users(models.Model):
#     name = models.CharField()
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.name


class Departments(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    departmentsid = models.ForeignKey(Departments, on_delete=models.CASCADE, verbose_name='Отдел', null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Statuses(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', default='in progress')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    name = models.IntegerField(verbose_name='Процент', default=15,)

    class Meta:
        verbose_name = 'Процент'
        verbose_name_plural = 'Проценты'


class Meals(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True,)
    description = models.CharField(max_length=100, verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'

    def __str__(self):
        return self.name


class Orders(models.Model):
    waiterid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Официант', null=True,)
    tablesid = models.ForeignKey(Tables, on_delete=models.CASCADE, verbose_name='Стол', null=True,)
    statusid = models.ForeignKey(Statuses, on_delete=models.CASCADE, verbose_name='Статус', null=True, )
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, verbose_name='Питание', null=True, )
    tablesname = models.CharField(max_length=100, verbose_name='Название стола')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата',)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.tablesname


class MealsToOrders(models.Model):
    count = models.IntegerField(default=1, verbose_name='Количество', null=True,)
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ', null=True,)
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, verbose_name='Питание', null=True,)

    class Meta:
        verbose_name = 'Распределение по заказам'
        verbose_name_plural = 'Распределение по заказам'


class Checks(models.Model):
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ', null=True)
    percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, verbose_name='Процент', null=True)
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата')
    mealsid = models.ForeignKey(Meals, on_delete=models.CASCADE, verbose_name='Питание', null=True)
    totalsum = models.CharField(max_length=100, verbose_name='Сумма')

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
