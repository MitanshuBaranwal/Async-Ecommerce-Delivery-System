from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializerInsert,UserSerializerVal
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer,OrderSerializerStatus
from .tasks import order_status_update
import send_email

# api for checking connection
def hi(request):
    return HttpResponse("Hello!")


class PlaceOrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Customize the logic for creating the order
        if serializer.is_valid():
            order_instance = serializer.save()

            # Get the user instance associated with the order
            user_instance = order_instance.user

            # Retrieve email and username from User model
            email = user_instance.email
            username = user_instance.username
            # Other details from the request data
            order_id = order_instance.order_id
            quantity = order_instance.quantity
            product_name = order_instance.product_name
            status = "Pending"
            company_name = order_instance.company_name

            # Schedule an asynchronous task to update order status
            order_status_update.apply_async((order_id,), countdown=60)

            # Send an email with order status details
            send_email.send_order_status_email(email, order_id, product_name, quantity, username, status, company_name)

# Create an API view for getting order details
class OrderDetailsAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

# Create an API view for retrieving order status details
class OrderStatusDetailsAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerStatus
    lookup_field = 'order_id'

# Create an API view for creating users
class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerInsert

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Create an API view for listing users
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerVal


