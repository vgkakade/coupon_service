from django.db import models


class CouponType(models.Model):
    """
    Represents a type of coupon.
    """

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Coupon(models.Model):
    """
    Represents a coupon that can be applied to an order.
    """

    code = models.CharField(max_length=30, unique=True)
    coupon_type = models.ForeignKey(CouponType, on_delete=models.CASCADE)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    min_cart_value = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usage_limit = models.PositiveIntegerField(default=1)
    valid_from = models.DateTimeField(
        blank=True, null=True, help_text="Start date for the coupon validity"
    )
    valid_to = models.DateTimeField(
        blank=True, null=True, help_text="End date for the coupon validity"
    )
    max_discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Maximum discount value for the coupon",
    )

    def __str__(self):
        return f"{self.code}"


class CouponRedemption(models.Model):
    """
    Represents a redemption of a coupon by a user.
    """

    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user_id = models.CharField(
        max_length=100, help_text="ID of the user who redeemed the coupon"
    )
    redeemed_at = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="ID of the order where the coupon was applied",
    )
    is_active = models.BooleanField(
        default=True, help_text="Indicates if the redemption is still valid"
    )

    class Meta:
        unique_together = ("coupon", "user_id", "order_id")

    def __str__(self):
        return f"{self.user.username} redeemed {self.coupon.code} on {self.redeemed_at}"


class CouponAssignment(models.Model):
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name="coupon_assignment"
    )
    user_id = models.CharField(
        max_length=50, help_text="User Id to whom coupon is assigned"
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("coupon", "user_id")

    def __str__(self):
        return f"Coupon {self.coupon.code} assigned to User {self.user_id}"
