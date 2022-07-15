# """ Custom Models and Generals Models """

from model_utils import models as custom_models

from django.contrib.auth.models import User
from django.db import models

class CustomModel(custom_models.TimeStampedModel, models.Model):
    """ Abstract Model with customizations.
    Adds a `timestamp` and `user` to create and update """
    created_by = models.ForeignKey(User, related_name='user_creation', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='user_update', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
