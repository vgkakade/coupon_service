from django.contrib import admin
from django.urls import path
from .views import AvailableCoupons

urlpatterns = [path("admin/", admin.site.urls), path("", AvailableCoupons.as_view())]
