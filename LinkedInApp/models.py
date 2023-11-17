from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, validators=[MinLengthValidator(14)])

    def __str__(self):
        return self.user.username