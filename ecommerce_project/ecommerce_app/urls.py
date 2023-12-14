# pizzeria/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('create_user/', views.CreateUserAPIView.as_view(), name='create_user'),
    path('user_list/', views.UserListAPIView.as_view(), name='user_list'),  # Add this line for user listing
    path('hi/', views.hi, name='hi'),  # get price for an order
    path('api/place_order/', views.PlaceOrderAPIView.as_view(), name='place_order_api'),
    path('api/order_details/<str:order_id>/', views.OrderDetailsAPIView.as_view(), name='order_details_api'),
    path('api/order_status_details/<str:order_id>/', views.OrderStatusDetailsAPIView.as_view(), name='order_status_details_api'),

]
