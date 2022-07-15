# """ Custom Models and Generals Models """

from model_utils import models as custom_models


from django.db import models

class CustomModel(custom_models.TimeStampedModel, models.Model):
    """ Abstract Model with customizations.
    Adds a `timestamp` to create and update """

    class Meta:
        abstract = True
