from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Bookcategory)
admin.site.register(models.book)
admin.site.register(models.Reviews)
