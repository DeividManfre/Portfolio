from django.db import models

class Color(models.Model):
    color = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("color")
        verbose_name_plural = ("colors")

    def __str__(self):
        return self.color

class Car(models.Model):
    COMPLETE = (
        ('S', 'Sim'),
        ('N', 'Não')
    )
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    complete = models.CharField(max_length=1, choices=COMPLETE, blank=False, null=False,default='N')
    yar = models.DateField(auto_now=False, auto_now_add=False)
    color = models.ForeignKey(Color, on_delete=models.RESTRICT)
    license_plate = models.IntegerField()

    class Meta:
        verbose_name = ("car")
        verbose_name_plural = ("cars")

    def __str__(self):
        return self.brand
