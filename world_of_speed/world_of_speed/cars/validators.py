from django.core.exceptions import ValidationError


def validate_car_year(year):
    if year < 1999 or year > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


