
from django.contrib import admin
# Register your models here.
from .models import Applicant
from .models import DatabaseRequest
from .models import EventModel


admin.site.register(Applicant)
admin.site.register(DatabaseRequest)
admin.site.register(EventModel)
