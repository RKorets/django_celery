from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'You subscribe to spam',
        'We send you more spam message.',
        'you_mail@gmail.com',
        [user_email],
        fail_silently=False,
    )
