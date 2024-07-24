from django.core.mail import send_mail
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.conf import settings

@receiver(email_confirmed)
def send_confirmation_email(request, email_address, **kwargs):
    user = email_address.user
    
    # Send email notification 
    subject = 'Account Successfully Verified' 
    message = ( 
        f'Dear {user.first_name},'
        '\n\nYour account has been successfully verified.\n' 
        'You now have full access to our booking platform. '
        'You can log in using your credentials.\n' 
        f'Your username is: {user.username}'
        '\n\nBest Regards,'
        '\nInfinita Perfectio' 
        ) 
    from_email = settings.DEFAULT_FROM_EMAIL 
    recipient_list = [user.email] 
    
    send_mail(subject, message, from_email, recipient_list)