from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class HobbyGroup(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    creator = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='created_groups'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    banner_url = models.URLField(
        blank=True,
        null=True
    )

    @property
    def members(self):
        return UserModel.objects.filter(groupmembership__group=self)

class GroupMembership(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        HobbyGroup,
        on_delete=models.CASCADE
    )
    joined_at = models.DateTimeField(
        auto_now_add=True
    )
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'group')
