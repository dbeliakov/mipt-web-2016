from django.contrib import admin
import forum.models

# Register your models here.

admin.site.register(forum.models.Category)
admin.site.register(forum.models.Thread)
admin.site.register(forum.models.Message)
