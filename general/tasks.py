from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def email(subject=None, body=None, from_email=None, to=None, template=None, template_data={}):
    if not to:
        raise Exception("No email recipient specified")

    if type(to) not in (tuple, list):
        to = [to]

    if template == 'forgot_password':
        subject = subject or "Password Recovery Link"
        body = body or "Please follow this link to reset your password: {}".format(template_data['link'])
    elif template == 'confirm_account':
        subject = subject or "Account Confirmation Link"
        body = body or "Please follow this link to confirm your account: {}".format(template_data['link'])

    send_mail(
        subject or "Email from {}".format(settings.SITE_NAME),
        body or "This email has no content",
        from_email or settings.DEFAULT_EMAIL_SENDER,
        to,
        fail_silently=False)
