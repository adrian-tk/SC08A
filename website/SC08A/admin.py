from django.contrib import admin

from .models import Question
from .models import Motor

admin.site.register(Question)
admin.site.register(Motor)

# Register your models here.
