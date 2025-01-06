from django.db import models


class CostDate(models.Model):
    year = models.IntegerField(verbose_name="年")
    month = models.IntegerField(verbose_name="月")
    day = models.IntegerField(verbose_name="日")
    food_cost = models.IntegerField(verbose_name="食費", null=True, blank=True)
    fixed_cost = models.IntegerField(verbose_name="固定費", null=True, blank=True)

    class Meta:
        db_table = "cost_date"
        constraints = [
            models.UniqueConstraint(
                fields=["year", "month", "day"], name="unique_cost_date"
            )
        ]

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
