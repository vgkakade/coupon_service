from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from core.models import CouponAssignment


class AvailableCoupons(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return CouponAssignment.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        codes = queryset.values_list("coupon__code", flat=True)
        return Response(list(codes), status=status.HTTP_200_OK)
