from django.db import models

# Create your models here.


class Applicant(models.Model):
    """Model for Applicant """

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

    def __str__(self):
        pass
