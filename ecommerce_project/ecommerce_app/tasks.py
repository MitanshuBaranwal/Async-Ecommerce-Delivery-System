from celery import shared_task
from django.utils import timezone
from .models import Order
import time
import send_email

@shared_task
def order_status_update(order_id):

    order = Order.objects.get(order_id=order_id)
    # Retrieve email and username from the related User model
    email = order.user.email
    username = order.user.username
    # Other details from the request data
    order_id = order.order_id
    quantity = order.quantity
    product_name = order.product_name
    company_name = order.company_name

    while True:
        current_time = timezone.now()
        elapsed_time = (current_time - order.order_date).total_seconds()
        print(elapsed_time)
        if elapsed_time < 120:
            order.status = 'Accepted'
            send_email.send_order_status_email(email, order_id, product_name, quantity, username, order.status, company_name)

        elif elapsed_time >= 180 and elapsed_time < 240:
            order.status = 'Dispatched'
            send_email.send_order_status_email(email, order_id, product_name, quantity, username, order.status, company_name)

        elif elapsed_time >= 240 and elapsed_time < 300:
            order.status = 'Out for Delivery'
            send_email.send_order_status_email(email, order_id, product_name, quantity, username, order.status, company_name)

        elif elapsed_time > 360:
            order.status = 'Delivered'
            send_email.send_order_status_email(email, order_id, product_name, quantity, username, order.status, company_name)
            order.save()
            break

        # Save the updated order status
        order.save()

        # Sleep for a while before checking again every minute
        time.sleep(60)