from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=120,verbose_name="Название")
    description = models.TextField(blank=True,verbose_name="Описание")
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Цена")
    rating = models.FloatField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"