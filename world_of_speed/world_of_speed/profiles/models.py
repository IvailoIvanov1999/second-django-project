from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from world_of_speed.profiles.validators import username_validator


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3
    MAX_PASSWORD_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH, message="Username must be at least 3 chars long!"),
            username_validator],
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        help_text="Age requirement: 21 years and above.",
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False)

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )
