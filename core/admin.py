from django.contrib import admin
from .models import CouponType, Coupon, CouponRedemption

@admin.register(Coupon)
class CouponTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'coupon_type', 'discount_value', 'is_active', 'min_cart_value', 'created_at', 'updated_at', 'usage_limit', 'valid_from', 'valid_to')
    search_fields = ('code', 'coupon_type__name')
    list_filter = ('is_active', 'coupon_type')


@admin.register(CouponType)
class CouponTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(CouponRedemption)
class CouponRedemptionAdmin(admin.ModelAdmin):
    list_display = ('coupon', 'user_id', 'redeemed_at', 'order_id', 'is_active')
    search_fields = ('coupon__code', 'user_id', 'order_id')
    list_filter = ('is_active',)
    raw_id_fields = ('coupon',)