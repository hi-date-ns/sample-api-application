from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import CostDate
from .serializers import CostDateSerializer


# Create your views here.
class CostDateViewSet(viewsets.ModelViewSet):
    queryset = CostDate.objects.all()  # 全てのCostDateデータを取得
    serializer_class = CostDateSerializer

    # POSTをUPSERTに変更
    def create(self, request, *args, **kwargs):
        data = request.data
        cost_date, created = CostDate.objects.update_or_create(
            year=data["year"],
            month=data["month"],
            day=data["day"],
            defaults={
                "food_cost": data.get("food_cost"),
                "fixed_cost": data.get("fixed_cost"),
            },
        )
        serializer = CostDateSerializer(cost_date)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)
