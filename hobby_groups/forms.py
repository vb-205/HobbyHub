from django import forms
from hobby_groups.models import HobbyGroup


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = HobbyGroup
        exclude = ['creator']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the group name',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter the group\'s description. This field is optional',
                'rows': 6,
            }),
            'banner_url': forms.TextInput(attrs={
                'placeholder': 'Enter the group\'s banner URL. This field is optional',
            }),
        }

class CreateHobbyGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        ...

class EditHobbyGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        ...