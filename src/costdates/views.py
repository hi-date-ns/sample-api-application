from rest_framework import viewsets

from .models import CostDate
from .serializers import CostDateSerializer


# Create your views here.
class CostDateViewSet(viewsets.ModelViewSet):
    queryset = CostDate.objects.all()  # 全てのCostDateデータを取得
    serializer_class = CostDateSerializer
