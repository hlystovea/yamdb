from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


def year_validator(value):
    if value > now().year:
        raise ValidationError(
            _('%(value)s год больше текущего'),  # noqa
            code='invalid',
            params={'value': value},
        )
