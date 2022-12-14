from django.contrib import admin
from . import models

admin.site.register(models.Subject)
admin.site.register(models.Teacher)
admin.site.register(models.Speciality)
admin.site.register(models.Group)
admin.site.register(models.Time)
admin.site.register(models.Lesson)


