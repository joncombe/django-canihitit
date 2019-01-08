import datetime
from django.conf import settings
from django.utils.timezone import now

from .models import TinyHitCount


def can_hitcount(request, object_type, object_id):
    return _can_hitcount(
        request.session.session_key,
        object_type,
        object_id,
        request.META['HTTP_USER_AGENT']
    )


def _can_hitcount(session_key, object_type, object_id, user_agent=None):
    seconds = getattr(settings, 'TINY_HIT_COUNTER_SECONDS', 300)
    cutoff = now() - datetime.timedelta(seconds=seconds)

    # ignore a few known bots. TODO: improve this
    if user_agent:
        user_agent = user_agent.lower()
        bots = 'baiduspider,bingbot,duckduckbot,exabot,facebookexternalhit,' \
               'facebot,googlebot,ia_archiver,sogou.com,yahoo! slurp,yandexbot'
        for b in bots.split(','):
            if b in user_agent:
                return False

    if TinyHitCount \
        .objects \
        .filter(object_type=object_type) \
        .filter(object_id=object_id) \
        .filter(session_key=session_key) \
        .filter(created__gte=cutoff) \
        .count() > 0:
        return False

    thc = TinyHitCount(
        object_type=object_type,
        object_id=object_id,
        session_key=session_key
    )
    thc.save()

    return True
