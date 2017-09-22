import time
from celery import task
from django.core.mail import send_mail


@task
def my_send_email(message,message_two,sender,receive,message_three):
    send_mail(message,message_two,sender,receive,html_message=message_three)
    time.sleep(5)