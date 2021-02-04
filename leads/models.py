from django.db import models


class Leads(models.Model):
    number = models.CharField(max_length=15, null=False)


    CNN = "Carinhanha"
    MLH = "Malhada"
    GNB = "Guanambi"
    PLM = "Palmas"

    MONTH_CHOICES = (
        (CNN, "Carinhanha"),
        (MLH, "Malhada"),
        (GNB, "Guanambi"),
        (PLM, "Palmas"),
    )

    city = models.CharField(max_length=50,
                    choices=MONTH_CHOICES,
                    default=CNN
                )
