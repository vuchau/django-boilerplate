from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def email(subject=None, body=None, from_email=None, to=None):
    if not to:
        raise Exception("No email recipient specified")

    if type(to) not in (tuple, list):
        to = [to]

    send_mail(
        subject or "Email from {}".format(settings.SITE_NAME),
        body or "This email has no content",
        from_email or settings.DEFAULT_EMAIL_SENDER,
        to,
        fail_silently=False)
