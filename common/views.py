from django.views.generic import TemplateView
from hobby_groups.models import GroupMembership, HobbyGroup


class HomePageView(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        user_group_ids = GroupMembership.objects.filter(user=user).values_list('group_id', flat=True)
        user_groups = HobbyGroup.objects.filter(id__in=user_group_ids)

        popular_groups = HobbyGroup.objects.exclude(id__in=user_group_ids)

        context['user_groups'] = user_groups
        context['popular_groups'] = popular_groups

        return context
