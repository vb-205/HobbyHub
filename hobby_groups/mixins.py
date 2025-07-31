from django.http import HttpResponseForbidden
from hobby_groups.models import GroupMembership

class GroupAdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()

        try:
            membership = GroupMembership.objects.get(user=request.user, group=group)
            if not membership.is_admin:
                return HttpResponseForbidden("Only group admins can perform this action.")
        except GroupMembership.DoesNotExist:
            return HttpResponseForbidden("You are not a member of this group.")

        return super().dispatch(request, *args, **kwargs)