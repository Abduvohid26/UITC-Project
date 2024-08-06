from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='users-images', default='default-image.jpg')
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} {self.username}'

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.check_hash_password()
        super(User, self).save(*args, **kwargs)
