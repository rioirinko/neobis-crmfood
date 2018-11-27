from django.contrib import admin
from .models import *
from users.models import Roles


class MyAdmin(admin.ModelAdmin):
    readonly_fields = ["totalsum", ]


admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(Departments)
# admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Orders)
admin.site.register(Tables)
admin.site.register(Statuses)
admin.site.register(Checks, MyAdmin)
admin.site.register(MealsToOrders)
admin.site.register(ServicePercentage)