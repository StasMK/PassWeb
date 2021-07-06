from django.db import models


# Create your models here.
class Articles(models.Model):
    troad = models.CharField('Титул дороги', max_length=10)
    nroad = models.CharField('Тиутльное наименование дороги', max_length=250)
    n_km = models.DecimalField('Начало участка', max_digits=7, decimal_places=3)
    k_km = models.DecimalField('Конец участка', max_digits=7, decimal_places=3)

    def __str__(self):
        return self.troad

    class Meta:
        verbose_name = 'Дорога'
        verbose_name_plural = 'Дороги'
