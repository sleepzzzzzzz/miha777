from django.db import models
from django.db.models import JSONField


class inputname(models.Model):
    field = models.CharField(max_length=30)
    text = JSONField()

    def __str__(self):
        return self.text, self.field
