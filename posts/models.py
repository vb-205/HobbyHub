from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from hobby_groups.models import HobbyGroup

UserModel = get_user_model()

class Post(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
        ]
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    group = models.ForeignKey(
        HobbyGroup,
        on_delete=models.CASCADE,
        related_name='posts'
    )

