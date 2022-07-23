from uuid import uuid4

from django.db import models


class UUIDidentifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class Timestamped(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True


class BaseModel(UUIDidentifier, Timestamped):
    class Meta:
        abstract = True
