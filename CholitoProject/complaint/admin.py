from django.contrib import admin
from complaint import models

# Register your models here.
admin.site.register(models.ComplaintImage)
admin.site.register(models.Complaint)
admin.site.register(models.AnimalType)