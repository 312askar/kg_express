from django.shortcuts import render
from django.views.generic import CreateView
from backend.apps.order.forms import OrderForm
from backend.apps.order.models import Order, OrderItem
# Create your views here.


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'order_create.html'
