from django.db import models


class Cart(models.Model):
    id_mahsol = models.IntegerField()

    def __str__(self):
        return str(self.id_mahsol)

