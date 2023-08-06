import phonenumbers
import logging
from phonenumbers import NumberParseException
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


def validate_format_e164_by_country(input_number, country_code="IN"):
    try:
        phone_number = phonenumbers.parse(input_number, country_code)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError("Invalid phone number")
        return phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.E164
        )
    except NumberParseException:
        logger.warn(
            "Failed to format number %s with country code %s"
            % (input_number, country_code)
        )
        return input_number
