from django.core import validators


class PhoneValidator(validators.RegexValidator):
    def __init__(self, *args, **kwargs):
        regex = r'^\+998\d{9}$'
        message = "Enter a valid phone number starting with +998 followed by 9 digits."
        super().__init__(regex=regex, message=message, *args, **kwargs)


phone_validator = PhoneValidator()


class UzCardValidator(validators.RegexValidator):
    def __init__(self, *args, **kwargs):
        regex = r'^\8600\d{12}$'
        message = "Enter a valid UzCard number starting with 8600 followed by 16 digits."
        super().__init__(regex=regex, message=message, *args, **kwargs)


class HumoCardValidator(validators.RegexValidator):
    def __init__(self, *args, **kwargs):
        regex = r'^\9860\d{12}$'
        message = "Enter a valid HumoCard number starting with 9860 followed by 16 digits."
        super().__init__(regex=regex, message=message, *args, **kwargs)


card_validators = [
    UzCardValidator(),
    HumoCardValidator()
]
