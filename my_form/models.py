from django.db import models
from django.db.models import JSONField
 
class MyFormModel(models.Model):
    json_field = JSONField()
 
