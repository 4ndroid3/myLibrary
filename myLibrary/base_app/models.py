# """ Contains custom models to use in the rest of the project """

from model_utils import models as custom_models

from django.contrib.auth.models import User
from django.db import models

class CustomModel(custom_models.TimeStampedModel, models.Model):
    created_by = models.ForeignKey(User, related_name='user_creation', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='user_update', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
