from rest_framework import serializers

from core.models import CouponAssignment


class CouponAssignmentSerializer(serializers.ModelSerializer):
    coupon_code = serializers.CharField(source="coupon", read_only=True)

    class Meta:
        model = CouponAssignment
        fields = ["coupon_code"]
