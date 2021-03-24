import django
from django.db import models


class Trade(models.Model):
  ticker = models.CharField(max_length=10)
  move = models.BooleanField(blank=True, null=True, default=True) #false for bearish and true for bullish
  time = models.DateTimeField(default=django.utils.timezone.now)

  def __str__(self):
    return self.ticker