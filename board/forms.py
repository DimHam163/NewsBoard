from django.core.exceptions import ValidationError

from board.models import Announcement, Comment
from django import forms


class AddAnnouncementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Announcement
        fields = ['title', 'text', 'image', 'category', 'url']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'Введите ваше сообщение : '
        }
