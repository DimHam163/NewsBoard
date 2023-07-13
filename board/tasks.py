import os

from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Announcement


@shared_task
def ann_created(announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    subject = f'Новое объявление: {announcement.title}'
    message = f'Приветствую,\n\n' \
              f'появилось новое объявление в категории {announcement.category},\n\n' \
              f'Быстрее смотреть!'
    mail_sent = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [User.email])
    return mail_sent
