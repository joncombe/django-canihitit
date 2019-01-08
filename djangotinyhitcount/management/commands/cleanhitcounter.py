import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from djangotinyhitcount.models import TinyHitCount


class Command(BaseCommand):
    def handle(self, *args, **options):
        seconds = getattr(settings, 'TINY_HIT_COUNTER_SECONDS', 300)
        cutoff = now() - datetime.timedelta(seconds=seconds)
        TinyHitCount.objects.filter(created__lte=cutoff).delete()
