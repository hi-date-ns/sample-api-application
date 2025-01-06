from rest_framework import serializers

from .models import CostDate


class CostDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostDate
        fields = "__all__"
