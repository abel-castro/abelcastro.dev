from django.contrib.auth.hashers import make_password
from django.db import models


class APIToken(models.Model):
    name = models.CharField(max_length=100)
    key_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def set_token(self, raw_token):
        self.key_hash = make_password(raw_token)
