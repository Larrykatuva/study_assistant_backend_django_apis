from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_writer = models.BooleanField(default=False)
    is_account = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.CharField(max_length=256, null=True)
    education_level = models.CharField(max_length=255, null=True)
    date_of_birth = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=256, null=True)
    institution = models.CharField(max_length=256, null=True)
    certificate = models.CharField(max_length=256, null=True)
    field = models.CharField(max_length=256, null=True)
    owner = models.ForeignKey(User, to_field='id', on_delete=CASCADE, unique=True)
