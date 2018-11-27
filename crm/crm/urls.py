"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from food import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tables/$', views.TablesViewSet.as_view(), name='tables',),
    url(r'^roles/$', views.RolesViewSet.as_view(), name='roles',),
    url(r'^departments/$', views.DepartmentsViewSet.as_view(), name='departments',),
    # url(r'^users/$', views.UserViewSet.as_view(), name='users',),
    url(r'^category/$', views.CategoryViewSet.as_view(), name='category',),
    url(r'^statuses/$', views.StatusesViewSet.as_view(), name='statuses',),
    url(r'^percentage/$', views.ServicePercentageViewSet.as_view(), name='percentage',),
    url(r'^meals/(?P<pk>[0-9]+)/$', views.MealsDetailView.as_view(), name='details',),
    url(r'^meals/$', views.MealsViewSet.as_view(), name='meals',),
    url(r'^orders/$', views.OrdersViewSet.as_view(), name='orders',),
    url(r'^checks/$', views.ChecksViewSet.as_view(), name='checks',),
    url(r'^mealstoorders/$', views.MealsToOrdersViewSet.as_view()),
    url(r'^tables/(?P<pk>[0-9]+)/$', views.TablesDetailView.as_view()),
    url(r'^roles/(?P<pk>[0-9]+)/$', views.RolesDetailView.as_view()),
    url(r'^departments/(?P<pk>[0-9]+)/$', views.DepartmentsDetailView.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UsersDetailView.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetailView.as_view()),
    url(r'^statuses/(?P<pk>[0-9]+)/$', views.StatusesDetailView.as_view()),
    url(r'^percentage/(?P<pk>[0-9]+)/$', views.ServicePercentageDetailView.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrdersDetailView.as_view()),
    url(r'^checks/(?P<pk>[0-9]+)/$', views.ChecksDetailView.as_view()),
    url(r'^mealstoorders/(?P<pk>[0-9]+)/$', views.MealsToOrdersDetailView.as_view()),
    url(r'^users/', include('users.urls', namespace='authentication')),
]
urlpatterns = format_suffix_patterns(urlpatterns)