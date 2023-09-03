from django.shortcuts import render,redirect
from cart.models import CartItem
from .models import Order, OrderProduct
from .forms import OrderForm
import datetime
# Create your views here.
def orders(request):
    return render(request,'order.html')
