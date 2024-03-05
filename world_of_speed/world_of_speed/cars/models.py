from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.cars.validators import validate_car_year
from world_of_speed.profiles.models import Profile


class Car(models.Model):
    MAX_CAR_TYPE_LENGTH = 10
    MAX_CAR_MODEL_LENGTH = 15

    CAR_TYPE_RALLY = "Rally"
    CAR_TYPE_OPEN_WHEEL = "Open-wheel"
    CAR_TYPE_KART = "Kart"
    CAR_TYPE_DRAG = "Drag"
    CAR_TYPE_OTHER = "Other"

    CAR_TYPE_CHOICES = (
        (CAR_TYPE_RALLY, CAR_TYPE_RALLY),
        (CAR_TYPE_OPEN_WHEEL, CAR_TYPE_OPEN_WHEEL),
        (CAR_TYPE_KART, CAR_TYPE_KART),
        (CAR_TYPE_DRAG, CAR_TYPE_DRAG),
        (CAR_TYPE_OTHER, CAR_TYPE_OTHER),
    )

    car_type = models.CharField(
        max_length=MAX_CAR_TYPE_LENGTH,
        choices=CAR_TYPE_CHOICES,
        null=False,
        blank=False
    )

    car_model = models.CharField(
        max_length=MAX_CAR_MODEL_LENGTH,
        validators=[MinLengthValidator(1)],
        null=False,
        blank=False
    )

    year = models.IntegerField(
        validators=[validate_car_year],
        null=False,
        blank=False
    )

    image_url = models.URLField(
        unique=True,
        error_messages={'unique': 'This image URL is already in use! Provide a new one.'},
        null=False,
        blank=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)],
        null=False,
        blank=False
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
