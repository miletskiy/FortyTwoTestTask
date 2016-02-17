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
        verbose_name=u'Name'
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=u'Last name'
    )
    birthday = models.DateField(
        blank=False,
        null=True,
        verbose_name=u'Birthday',
        help_text=u'Please use the following format: <em>YYYY-MM-DD</em>'
    )
    bio = models.TextField(
        blank=True,
        verbose_name=u'Bio'
    )
    email = models.EmailField(
        max_length=50,
        blank=False,
        verbose_name=u'Email'
    )
    jabber = models.EmailField(
        max_length=50,
        blank=True,
        verbose_name=u'Jabber'
    )
    skype = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=u'Skype'
    )
    contacts = models.TextField(
        blank=True,
        verbose_name=u'Other contacts'
    )

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)


class DatabaseRequest(models.Model):

    class Meta:
        verbose_name = "DatabaseRequest"
        verbose_name_plural = "DatabaseRequests"
        ordering = ['-emergence']

    title = models.CharField(
        max_length=30,
        verbose_name="Title",
        default="Request in database"
    )
    emergence = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date time of the emergence"
    )
    path = models.CharField(
        max_length=100,
        verbose_name="Request path"
    )
    method = models.CharField(
        max_length=4,
        verbose_name="Request method"
    )
    user = models.CharField(
        max_length=42,
        verbose_name="User",
        blank=True
    )

    def __unicode__(self):
        return u'{} {}'.format(self.title, self.emergence)
