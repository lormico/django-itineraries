from django.db import models


class Tranche(models.Model):
    id = models.CharField('ID', primary_key=True)
    short_descr = models.CharField('Short Description')
    order = models.IntegerField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.short_descr
