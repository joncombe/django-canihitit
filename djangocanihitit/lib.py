import datetime
from django.conf import settings
from django.utils.timezone import now

from .models import CanIHitIt


def canihitit(request, object_type, object_id):
    if request.method in ['GET', 'POST']:
        return _canihitit(
            request.session.session_key or request.META.get('REMOTE_ADDR', None) or '',
            object_type,
            object_id,
            request.META.get('HTTP_USER_AGENT', None)
        )
    else:
        return False


def _canihitit(session_key, object_type, object_id, user_agent=None):
    seconds = getattr(settings, 'CAN_I_HIT_IT_SECONDS', 300)
    cutoff = now() - datetime.timedelta(seconds=seconds)

    # ignore a few known bots. TODO: improve this
    if user_agent:
        user_agent = user_agent.lower()
        bots = [
            'apachebench', # not a bot, but it can go here

            '360spider',
            'adsbot-google',
            'ahrefs',
            'archive.org',
            'baiduspider',
            'bingbot',
            'bingpreview',
            'dotbot',
            'duckduckgo',
            'duckduckbot',
            'exabot',
            'facebook',
            'feedfetcher-google',
            'googlebot',
            'googleimageproxy',
            'ia_archiver',
            'mediapartners-google',
            'mj12bot',
            'msnbot',
            'panscient.com',
            'pinterest',
            'slackbot',
            'slurp',
            'sogou',
            'surveybot',
            'twitterbot',
            'voilabot',
            'yahoo-mmcrawler',
            'yahoomailproxy',
            'yandexbot'
        ]
        for b in bots:
            if b in user_agent:
                return False

    if CanIHitIt \
        .objects \
        .filter(object_type=object_type) \
        .filter(object_id=object_id) \
        .filter(session_key=session_key) \
        .filter(created__gte=cutoff) \
        .count() > 0:
        return False

    cihi = CanIHitIt(
        object_type=object_type,
        object_id=object_id,
        session_key=session_key
    )
    cihi.save()

    return True
