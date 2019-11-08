from django.contrib import admin
from stdapp.models import User,Course,Batch,Feedback
# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Feedback)