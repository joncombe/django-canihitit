from django.conf import settings
from django.db import models


class TinyHitCount(models.Model):
    object_type = models.CharField(max_length=32, db_index=True)
    object_id = models.IntegerField(db_index=True)
    session_key = models.CharField(max_length=40, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s: %s#%s' % (self.id, self.object_type, self.object_id)
