from django.core.exceptions import ValidationError

def validate_acceptable_cost_to_make(value):
    if value > 5.00:
        raise ValidationError('Unable to accept items that cost more than $5.00 to make.')
