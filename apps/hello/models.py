from django.db import models
from PIL import Image
# Create your models here.
from django.contrib.auth.models import User


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
    photo = models.ImageField(
        upload_to='photo',
        blank=True,
        max_length=100,
        default=''
    )

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):

        size = (200, 200)
        if self.photo:
            super(Applicant, self).save(*args, **kwargs)

            img_object = Image.open(self.photo)
            if img_object.mode not in ("L", "RGB"):
                img_object = img_object.convert("RGB")
            img_object.thumbnail(size, Image.LANCZOS)
            img_object.save(self.photo.path)

        super(Applicant, self).save(*args, **kwargs)


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
    user = models.ForeignKey(
        User,
        verbose_name="User",
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u'{} {}'.format(self.title, self.emergence)
