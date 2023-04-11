from django.contrib import admin
from accounts import models

admin.site.register(
    [
        models.Patient,
        models.Doctor,
        models.Staff,
        
    ]
)


# Register your models here.
