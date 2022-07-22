# """ Custom Models and Generals Models """

from django.db import models
from model_utils import models as custom_models

class CustomModel(custom_models.TimeStampedModel, models.Model):
    """ Abstract Model with customizations.
    Adds a `timestamp` to create and update """

    class Meta:
        abstract = True
