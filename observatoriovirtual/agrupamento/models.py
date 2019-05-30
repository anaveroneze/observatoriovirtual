from django.db import models


class FoFAlgorithm(models.Model):
    idFoF = models.AutoField(primary_key=True)
    nameFoF = models.CharField(null=False, blank=False, max_length=100)
    descFoF = models.TextField(null=True, blank=False)
    commandFoF = models.TextField(null=False, blank=False)


    class Meta:
        managed = True
        db_table = 'fof_algorithm'

    def __str__(self):
        return self.nameFoF
