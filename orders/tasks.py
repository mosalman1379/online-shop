from onlineshop.celery import app
from django.core.mail import send_mail
from orders.models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order num:{order.id}'
    message = f'Dear {order.first_name},' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}'
    mail_sent = send_mail(subject, message, 'mosalman1379@gmail.com', [order.email])
    return mail_sent
