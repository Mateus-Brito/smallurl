from django.db import models
from smallurl.core.models import BaseModel
from smallurl.core.utils import generate_code


class Shortener(BaseModel):
    full_url = models.URLField()
    hash_url = models.CharField(max_length=15, unique=True)
    times_followed = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "urls"
        verbose_name = "url"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.full_url} -> {self.hash_url}"

    def follow(self):
        self.times_followed += 1
        self.save()

    def generate_hash_url(self):
        code = generate_code()
        while self.__class__.objects.filter(hash_url=code).exists():
            code = generate_code()
        self.hash_url = code

    def save(self, *args, **kwargs):
        if not self.hash_url:
            self.generate_hash_url()

        return super().save(*args, **kwargs)
