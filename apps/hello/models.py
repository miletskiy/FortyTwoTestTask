from django.db import models

# Create your models here.


class Applicant(models.Model):
    """Model for Applicant """

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

    first_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Name'
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Last name'
    )
    birthday = models.DateField(
        blank=False,
        null=True,
        verbose_name='Birthday',
        help_text='Please use the following format: <em>YYYY-MM-DD</em>'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Bio'
    )
    email = models.EmailField(
        max_length=50,
        blank=False,
        verbose_name='Email'
    )
    jabber = models.EmailField(
        max_length=50,
        blank=True,
        verbose_name='Jabber'
    )
    skype = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Skype'
    )
    contacts = models.TextField(
        blank=True,
        verbose_name='Other contacts'
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
