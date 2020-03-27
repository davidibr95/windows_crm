from django import forms
from mainapp.models import Tasks


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['user', 'message', 'todo_date', 'completed']
        widgets = {
            'todo_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        if not self.request.user.is_superuser:
            self.fields['user'].queryset = self.fields['user'].queryset.filter(
                pk=self.request.user.pk
            )

    def save(self, commit=True):
        instance = super(AddTaskForm, self).save(commit=commit)
        if self.request:
            instance.creator = self.request.user
            instance.save()
