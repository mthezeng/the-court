from django.contrib import admin
from .models import Case, Opinion, Justice

# Register your models here.
admin.site.register(Case)
admin.site.register(Opinion)
admin.site.register(Justice)
