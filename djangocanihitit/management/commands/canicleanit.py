import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from djangocanihitit.models import CanIHitIt


class Command(BaseCommand):
    def handle(self, *args, **options):
        seconds = getattr(settings, 'CAN_I_HIT_IT_SECONDS', 300)
        cutoff = now() - datetime.timedelta(seconds=seconds)
        CanIHitIt.objects.filter(created__lte=cutoff).delete()
